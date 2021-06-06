
# How to use Makefiles to run a simple Map Reduce Data Pipeline

**Link:** https://www.benevolent.com/engineering-blog/make-reduce-how-to-use-makefiles-to-run-a-simple-map-reduce-data-pipeline

# Why use Make

Benefits of Make

* Ubiquity
* Maintenance - is easy, dont need large cluster
* Draft development - easy to design so rapid feedback, can check core modules before moving onto a more powerful tool
* Shell - Using Unix Philosophy and linking programs together enables you to very quickly put together programs written in various languages
* Simple - Conceptual framework of dependency graph is well defined in Makefiles



# Background

## Map Reduce

Well-used technique for parallel processing. Most useful for distributing jobs among large clusters with many distributed resources. Dont always need large clusters to get the benefit of the paradigm

## Make

40+ yrs old, known as a build tool for compiling C programs, or as a way of tracking small aliases in a directory for functions like "install" or "clean". Fundamentally, its job is to be a schedular.

## Features of Make Important for Pipelines and Map Reduce

1. Dependency Graph - it ingests a Directed Acyclic Graph of rules known as a *Makefile*.
2. Topological Order or Rule Execution - it executes rules in *topological order*; meaning  all the prerequisite rules are executed first. The **target** rules are executed if and only if the prerequisites have completed successfully.
3. Smart Restart of Rule Execution - If a large pipeline needs to restart, it will only execute rules with modified dependencies, meaning it will NOT execute rules that have already run.

# Make and Makefiles Refresher

## A Rough Sketch of Make

1. make executes the dependency of graphs defined in Makefiles
2. *Makefiles* are made up of **rules** which define a rule's **target**, the rules **prerequisites**, and the **recipe** that updates the **target**
3. When we call make from the CL we're giving it a make **goal** to update
4. make will execute all **rules** in the required order to satisfy the **goal**
5. make will skip **rules** that already have completed **targets**

## Variables

Variables are assigned using the `=` operator. Convention is variable names are all caps, as they're considered as constants. They are defined at the beginning of execution and do not change during each call to make. We can also pass variables to make via the CL.

## Special Variables

Special variables help us create reusable recipes:

* $@ -> the target rule
* $< -> the 1st normal prerequisite
* $^ -> all normal prerequisites
* $| -> all order-only prerequisites

## Phony Tagerts

In Unix, *Everything is a File* including targets. However with Make Reduce, we have a convention: if a target doesn't have a file extension, then it doesn't represent a file to be updated. Is known as a *Phony Target*, simply a name for the recipe that will be executed.


```{bash}

# Variables
GOAL=goodbye.txt
START=hello.txt

# Special Variables
$(START):
	echo "hello world!" > $@

$(GOAL): $(START)
	cat $< > $@
	echo "good bye!" >> $@

# Phony Target
bye: $(GOAL)

```


# Make Reduce Tutorial

Will work with a typical example of Map Reduce: word counting. The **Goal** is to count all unique words in some group of text files.

## Pipeline Plan

1. We will grab some text files from gutenberg (Initialisation)
2. We will clean each text file (Map)
3. We will cont the words in each cleaned file (Map)
4. We will sum up all of the counted words and merge them together (Reduce)

Tasks marked with Map are considered **obviously parallel**: task 2 can operate on each file independently; the cleanliness of each file in task 2 is irrelevant to the cleanliness of every other file in task 2. Task 3 is **obviously parallel** in that the word count for each file is irrelevant to every other file in task 3. Finally, the reduce step adds up everything and outputs a count file.

# Makefile

Note on writing Makefiles: if you get an error like `Makefile:20: *** missing separator.  Stop.`, check the tabs and spacing are okay using `cat -e -t -v Makefile`, as shown in https://stackoverflow.com/questions/16931770/makefile4-missing-separator-stop

## Pipeline Step 1: Initialize

Can begin building out *Makefile*. We'll start with a few initialisation variables: what directory our source text files will be downloaded to and what directory our work will be stored in.

```{bash}

# Initial variables for workspace
WORK_DIR?=$(PWD)/make_reduce
DOWNLOAD_DIR=$(WORK_DIR)/download
DATA_DIR=$(WORK_DIR)/data
FINAL_OUTPUT=$(WORK_DIR)/finalcount

```

We'll start with a simple **rule** init, to initialize and download. We want our rule's **recipe** to do the following:

  1. Create the necessary directories for workspaces if they don't exist
  2. Download all the text files required
  3. Soft link all the text files to a single directory for simpler viewing.

Download files from *Project Gutenberg*. In order to follow their robot policy, we'll rsync files from a mirror at *aleph.gutenberg.org*.The LIMITSIZE variable allows us to download only about 1000 files by limiting the files available for download to 100kb-105kb. If we set the LIMITSIZE variable to blank, we will download all ~100,000 serially and it could take an hour or so.

```{bash}
# Makefile continued

# argument to limit the size of download.
# Set to empty to download all of gutenberg
LIMITSIZE=--min-size=100K --max-size=105K

# Download gutenberg files
$(DOWNLOAD_DIR):
  mkdir -p $@
  rsync -avz $(LIMITSIZE) --del --include="*/" --include="*.txt" --exclude="*" aleph.gutenberg.org::gutenberg $@

# Softlink downloaded files to a workspace directory
$(DATA_DIR): $(DOWNLOAD_DIR)
  mkdir -p $@
  find $< -name '*.txt' -exec ln -sf {} $@ \;

# Phony init target
init: | $(DATA_DIR)

```

To execute the initialisation rules, run the following command:

```{bash}
# Shell

make init

```

In this command, we've told make that out **goal** is to create or update the *./make_reduce/data* directory. make reviews the dependency graph in the *Makefile*, then topologically sorts and determines the correct order of operations and then executes all the **recipes** required. We've fed it a grpah and it is executing it for us!

Once it completes, you should see something similar to the output below: We have downloaded all the files and them soft linked them;

```{bash}
# Shell

make init

```

Should be able to see all the downloaded files in the DOWNLOAD_DIR:

```{bash}
# Shell

tree ./make_reduce/download | head

```

The directory structure from gutenberg is a bit messy, which is why we soft linked all the `.txt` files to a single directory.

```{bash}
# Shell

ls -l ./make_reduce/data | head -4

```

And the files count:

```{bash}
# Shell

ls ./make_reduce/data | wc -l

```

About 1000 text files on which we want to perform word count on.



## Pipeline Step 2: Clean Text File

Will write clean function in Python. It first reads a file into memory, lowercases all the characters, removes all punctuation, and removes any tokens that are less than three characters long. It then outputs the cleaned text files with one word per line into an output file:

```{python}

import sys
import re
import string

TRANSLATOR=str.maketrans(' ',' ', string.punctuation)

def clean(text):

    cln = text.lower()

    # strip out punctuation
    cln = cln.translate(TRANSLATOR)
    cln = re.sub('\s+', ' ', cln)

    # clean out words that are less than or equal to 2 chars
    toks = cln.split(' ')
    # put each word on a new line for easier reading
    cln = '\n'.join(t for t in toks if len(t) >= 3)

    return cln


if __name__ == '__main__':

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # get text string
    text = open(infile, encoding='utf-8', errors='ignore').read()

    # clean the text
    outstr = clean(text)

    # write final output
    with open(outfile, 'w') as out:
        out.write(outstr)

```

Let's encode the clean step into out *Makefile* using the following strategy.

1. Use the **wildcard** function to assign a list of input file paths into a variable
2. Use the string substitution to create a list of output file paths.

Create a *Match-Anything Pattern Rule* which links each input file name to the output filename.

```{bash}

# Make Reduce Makefile continued

# Take all txt file paths and put into single variable		
TXTFILES=$(wildcard $(DATA_DIR)/*.txt)
CLEANFILES=$(TXTFILES:%.txt=%.cln)

# Rule for creating the filenames with *.cln extension
clean: $(CLEANFILES)

# Rule that updates the target *.cln file from the prerequisite *.txt file
%.cln: %.txt
		python clean.py $<  $@

```

```{bash}
# Shell

make clean

```

We can see the creation of the `*.cln` files in our `WORK_DIR`

```{bash}
# Shell

head ./make_reduce/data/10133-8.cln

```

## Aside: Parallelisation

Each pair of `*.txt` & `.cln` files are independent of each other pair. This means that they have now become **obviously parallel**. make has a critical directive that we can pass from the command line to process each of the independent targets in parallel: `-j` or `--jobs`, or # jobs to run in parallel.

```{bash}
# Shell

make clean -j

```


## Pipeline Step 3: Count words in each file

Each `*.cln` file needs to be counted. Will use a simple BASH command for this task in the script (`count_cln.sh`):

```{bash}
#!/bin/bash
INFILE=$1
OUTFILE=$2

sort "${INFILE}" | uniq -c | sort -rn > "${OUTFILE}"

```

```{bash}
# Makefile continued

COUNTS=$(TXTFILES:%.txt=%.cnt)
count: $(COUNTS)
%.cnt: count_cln.sh %.cln
		bash $^ $@

```

We add the executable `count_cln.sh` as a prerequisite because if we change the count function, make will automatically rerun the count step. We will automatically restart parts of the pipeline only from the steps that have either new data or a new function. We change our special variable from `$<` to `$^` so that all **normal prerequesites** are passed to the recipe.

```{bash}

make count -j

```


## Pipeline Step 4: Reduce

Now we have run the clean and count (Map) steps, we need to perform the reduce step. We will use out `$^` variable again to pass in all of the **normal prerequisites** to the **recipe**.


```{bash}
# Makefile continued

# Reduce all of the count file to a single file using awk
reduce: $(FINAL_OUTPUT)
$(FINAL_OUTPUT): $(COUNTS) 	
		awk '{ count[$$2] += $$1 } END { for(elem in count) print count[elem], elem }' $^ | sort -rn > $@

```

And run it:

```{bash}

make reduce

```


## Executing Entire Pipeline with a Single Command

Can put al steps together in their own **phony target**. We define a **goal** pipeline that will execute all of the make commands recursively from the shell using the special `$(MAKE)` variable. Can set our parallel parameters with the `-j` directive and end with `reduce`

```{bash}
# Makefile continued

pipeline:
		$(MAKE) init
		$(MAKE) clean -j
		$(MAKE) count -j
		$(MAKE) reduce

```

We can force the pipeline to execute via a couple of different ways; either passing a new `WORK_DIR` or with the force directive `-B`.

```{bash}
make pipeline WORK_DIR=/usr/local/data/make_reduce/gutenberg
```

```{bash}
make pipeline -B
```


## Scale

If we want to increase the number of files being operated on, we can change the variables, namely LIMITSIZE, on the command line argument. The init step downloading the data will be the bottleneck, `rsync` will help reduce duplicate downloads, but it will still be the slowest point.

```{bash}
make pipeline WORK_DIR=/usr/local/data/make_reduce/gutenberg LIMITSIZE=”” -B
```
