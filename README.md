# PassCheck

## usage

Run the following commands. Replace `...` with your password. Note, keep the quotes in the
command.

```bash
$ git clone ...
$ cd passcheck
$ ./passcheck.py '...'
```

PassCheck will return one of `WEAK`, `OK`, `STRONG`. Strong passwords must be more than
5 characters, contain a number, and contain a special character. If only two conditions
are met, then the password will be `OK`. Otherwise, the password will be `WEAK`.

## limitations

This tool is for educational use only and should not be used for securing sensitive information.
The password evaluations are not meant to be indicative of actual password strength.
As such, this program should not be used in any production level software.
