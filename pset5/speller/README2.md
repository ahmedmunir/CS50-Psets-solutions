# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

TODO
A word inside a text that will be checked whether it is exist inside dictionary or not.

## According to its man page, what does `getrusage` do?

TODO
it takes argument (in out case RESAGE_SELF) that return resource usage statistics for the calling process 
(sum of them) according to structure we pass whether it before using or after using some resources.

## Per that same man page, how many members are in a variable of type `struct rusage`?

TODO
16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

TODO
to be able to get user CPU time used and other parameters in real-time.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

TODO
first of all, it open file and assign that file address to pointer, then check whether this pointer points to
NULL or not, then makeing for loop, this for loop will stop when we reach to end of file, it will read characters
one by one, it will everytime check whether it is alpha or not and if it is,it will assign it to array of
characters and increase the index by 1, if the index becomes larger than 45 which is the maximum lengh of
string, the index value will be assigned to zero to read a new word.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

TODO
because sometimes and for some reasons, fscanf stucks at reading lines and never reach to EOF so it will 
stuck at infinite loop for ever

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

TODO
To not able to change them, you can't apply any modification to them at any function, and this can be useful
with pointers, global variables, and local variable at the same function to avoid any modification to them.
