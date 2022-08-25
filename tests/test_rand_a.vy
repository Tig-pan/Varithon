# this is essentially rand(0, rand(0, rand(0, 100)))
# thus it should be expected that it will output a very low number

~[var a]~ = ~[rand -i 0 {rand -i 0 {rand -i 0 100}}]~
print(~[get a]~)