import pandas as pd

new_rows_from_full_data = ["hhidpn", "r1deprex", "r1efforx", "r1sleepx", "r1whappx", "r1flonex", "r1fsadx",
                           "r1goingx", "r1enlifx", "r2cesd", "r3cesd", "r4cesd", "r5cesd", "r6cesd", "r7cesd", "r8cesd",
                           "r9cesd", "r10cesd", "r11cesd", "hacohort", "racohbyr", "raedyrs", "r1proxy", "r2proxy",
                           "r3proxy", "r4proxy", "r5proxy", "r6proxy", "r7proxy", "r8proxy", "r9proxy", "r10proxy",
                           "r11proxy"]


df = pd.read_stata("rndhrs_o.dta", columns=new_rows_from_full_data, convert_categoricals=False, convert_dates=False)
df.to_csv("rndhrs_o.csv")