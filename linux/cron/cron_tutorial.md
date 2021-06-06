
# Scheduling Cron Jobs with Crontab

**Date:** https://linuxize.com/post/scheduling-cron-jobs-with-crontab/

Cron is a scheduling daemon that executes tasks at specified intervals. Called **cron jobs** mostly used to automate sys maintenance and admin.

## Crontab File

Crontab (cron table). 2 types - system-wide & individual. Can manually edited crontab files, recommended to use `crontab`.

* Individual - User's crontab files named acording to the user's name, location & varies by OS. Ie in Red Hat based distributions ie CentOS, they're stored in `/var/spool/cron` while on Debina and Ubuntu they're in `/var/spool/cron/crontabs` directory.
* System-wide - the `/etc/crontab` file and scripts inside `/etc/cron.d` directory are system-wide that can be edited only by the sys admins. In most Linux distributions, you can also put scripts inside the `/etc/cron.{hour,daily,weekly,monthly}` directories and scripts will be executed every `hour/day/week/month`.


# Crontab Syntax & Operators

Each line in the user crontab file contains 6 fields separated by a space followed by the command to run

```
* * * * * command(s)
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)
```

1st 5 fields contain one or more values, separated by a comma or range of values separated by a hyphen.

* `*` - Asterisk operator means any value or always. Ie if in hour field, means it will be performed eveey hour
* `,` - Comma operator allows you to specify a list of values for repetition. Ie `1,3,5` in Hour field, will run at 1am, 3am & 5am.
* `-` - Hyphen operator allows you to specify a range of values, if you have `1-5` in days of the week field, the task will run every weekday.
* `\` - Slash operator allows you to specify values to be repeated over a certain interval between them. Ie `*/4` in the hour field, it means the action will be performed every 4 hours. Same as specifying `0, 4, 8, 12, 16, 20`. Instead of an asterisk before the slash operator, you can also use a range of value, `1-30/10` is the same as `1,11,21`.


# System-wide Crontab Files

Slightly different, includes an extra mandatory user field that specifies which user will run the cron job.


# Predefined macros

Several special Cron schedule macros used to specify common intervals. Can be used in place of 5-column date-specification:

* `@yearly` (`@annually`) - Run the specified task once a year at midnight (12:00 am) of the 1st of Jan, equiv of `0 0 1 1 *`
* `@monthly` - Run the specified task once a month on the 1st day of the month, equiv to `0 0 1 * *`
* `@weekly` - Run the specified task once a week at midnight on Sunday, equiv to `0 0 * * 0`
* `@daily` - Run the specified task once a day at midnight, equiv to `0 0 * * * `
* `@hourly` - Once an hour at the beginning of the hour, equiv to `0 * * * *`
* `@reboot` - start the specified task at the system startup (boot-time)


# Linux Crontab command

The `crontab` comman allows you to install, view or open a crontab file for editing:

* `crontab -e` - edit, or create if it doesn't exist
* `crontab -l` - display crontab file contents
* `crontab -r` - remove current crontab file
* `crontab -i` - remove your current crontab file with a prompt before removal
* `crontab -u <username>` - edit other user crontab file. Requires sys admin priveledges.


# Crontab variables

The cron daemon automatically sets several *environmental variables*.

* Defauly path is set to `PATH=/usr/bin:/bin`. If the command you are executing isn't present in the cron specified path, you can either use the abs path to the command or change the cron `$PATH` variable. Can't implicitly append `:$PATH` as you would with a regular script.
* The default shell is `/bin/sh`, to change use the `SHELL` variable.
* Cron invokes the command from the user's home directory. The `HOME` variable can be set in the crontab
* The email notification is sent to the owner of the crontab. To overwrite the default behaviour, you could use the `MAILTO` environment variable with a list (comma separated) of all email addresses you want to recieve the email notifications. When `MAILTO` is defined but empty (`MAILTO=""`), no mail is sent.


# Crontab restrictions

The `/etc/cron.deny` and `/etc/cron.allow` files allows sys admins to control whuch users have access to the `crontab` command. The file consists of a list of usernames, one user name per line, which are added manually. While `/etc/cron.deny` exists but is blank by default, if `/etc/cron.allow` exists, only users who are listed in this file can use the `crontab` command. If neither exists, only users with admin priveledges can use it.
