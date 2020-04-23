load harness

@test "my_test-1" {
  check 'a := 98 ; b := 76 ; while ( a > b ) do { if a < 100 then b := a else a := b }' '{a → 98, b → 98}'
}

@test "my_test-2" {
  check 'if false then k := 12 else while false do l := 0 ; if x > z then x := 5 else x := 4' '{x → 4}'
}

@test "my_test-3" {
  check 'a := 5 ; b := -1 ; while ¬ ( a = b ) do { if a < b then b := a else a := b }' '{a → -1, b → -1}'
}

@test "my_test-4" {
  check 'i := -1 ; fact := 1 ; while 0 < i do { fact := fact * i ; i := i - 1 }' '{fact → 1, i → -1}'
}

@test "my_test-5" {
  check 'if ( true ) then y := 1 else z := y * 5 + 6' '{y → 1}'
}

@test "my_test-6" {
  check 'if ( false ) then y := 1 else z := y * 5 + 6' '{z → 6}'
}