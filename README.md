# TDR
Threat Detection and Response - SOAR


## How to run:

1. Create virtual environment, source it, and install requirements.txt
2. To run dissimilation:
   >python3 runner.py --file_path=absolute/path/to/sample.txt 
   --model_type=dissimilarity --start_row=1 --start_column=1 --row_size=3 --column_size=3
   
3. To run Schelling model:
    >python3 runner.py --file_path=absolute/path/to/sample.txt --model_type=schelling --threshold=0.3 --iterations=20
   > 
4. To run the tests:
   >python3 -m pytest
