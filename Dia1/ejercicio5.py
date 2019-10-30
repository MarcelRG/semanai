import pandas as pd
ser = pd.Series(["how", "to", "kick", "ass?"])
ser.map(lambda x:x.title())