~[var a]~ = ~[collection -b {rand -i 3 5} {rand -f 0 100}]~

for ~[var b]~ in ~[get a]~:
    print(~[get b]~)