# Initial variables for workspace
WORK_DIR?=$(PWD)/make_reduce
DOWNLOAD_DIR=$(WORK_DIR)/download
DATA_DIR=$(WORK_DIR)/data
FINAL_OUTPUT=$(WORK_DIR)/finalcount





# Step 1: Initialization: Download files

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





# Step 2: Map: Clean text files

# Take all txt file paths and put into single variable
TXTFILES=$(wildcard $(DATA_DIR)/*.txt)
CLEANFILES=$(TXTFILES:%.txt=%.cln)

# Rule for creating the filenames with *.cln extension
clean: $(CLEANFILES)

# Rule that updates the target *.cln file from the prerequisite *.txt file
%.cln: %.txt
		python clean.py $<  $@






# Step 3: Map: Count words in cleaned file

# Makefile continued

COUNTS=$(TXTFILES:%.txt=%.cnt)
count: $(COUNTS)
%.cnt: count_cln.sh %.cln
		bash $^ $@





# Step 4: Reduce: 


# Reduce all of the count file to a single file using awk
reduce: $(FINAL_OUTPUT)
$(FINAL_OUTPUT): $(COUNTS) 	
		awk '{ count[$$2] += $$1 } END { for(elem in count) print count[elem], elem }' $^ | sort -rn > $@





# Run Pipeline with one Command

pipeline:
		$(MAKE) init
		$(MAKE) clean -j
		$(MAKE) count -j
		$(MAKE) reduce
