#!/usr/bin/python3

print("".join([chr(i) for i in range(97, 123) if i not in (ord('q'), ord('e'))]), end="")
