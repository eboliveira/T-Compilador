; ModuleID = "module.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"soma"(i32 %".1", i32 %".2") 
{
entry:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %"b" = alloca i32
  store i32 0, i32* %"b"
  br label %"body"
body:
  %".7" = load i32, i32* %"a"
  %".8" = load i32, i32* %"b"
  %".9" = add i32 %".7", %".8"
  ret i32 %".9"
}

define i32 @"main"() 
{
entry:
  br label %"body"
body:
  %"body_a" = alloca i32
  store i32 0, i32* %"body_a"
  %"body_b" = alloca i32
  store i32 0, i32* %"body_b"
  %"body_c" = alloca i32
  store i32 0, i32* %"body_c"
  ret i32 0
}
