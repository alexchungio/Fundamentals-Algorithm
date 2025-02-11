## ## install

### gdb

* step0
  ```
  brew install gdb
  ```
* step1
  ```
  $ witch gdb
  ```
* step2
  generate key-sign and named `gdb-cert`
* step3
  ```
  $ codesign --entitlements gdb-entitlements.yaml -fs gdb-cert /usr/local/bin/gdb 
  ```
* step4
  ```
  $ echo "set startup-with-shell off" >> ~/.gdbinit
  ```

## build command

### g++

* build

  g++ main.cpp -o main -lpthread -std=c++11 -g # linux | macos
  clang++ main.cpp -o main -lpthread -std=c++11 -g # macos
* run

```
  gdb ./main
```

### cmake
