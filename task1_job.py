import os
import sys
import argparse
import pandas as pd

DEFAULT_INPUT_FNAME = './input/hacker_news_data.json'
DEFAULT_OUTPUT_FNAME = './output/hourly_agg.csv'

def job(df: pd.DataFrame) -> None:
    df.assign(words_in_title=df['title'].str.split().str.len().fillna(0)) \
          .groupby(df['time'].apply(lambda ts: pd.to_datetime(ts, unit='s')).round('H')) \
          .agg(mean_score=('score', 'mean'),
               median_score=('score','median'),
               num_words_in_titles=('words_in_title','sum'),
               max_id=('id','max'),
               sum_descendants=('descendants','sum'),
              ) \
            .convert_dtypes() \
            .to_csv(args.output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', type=str, default=DEFAULT_INPUT_FNAME, help='input file name')
    parser.add_argument('-o','--output', type=str, default=DEFAULT_OUTPUT_FNAME, help='output file name')
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print('There is no such file path: ', args.input)
        sys.exit(1)
    
    try:
        df = pd.read_json(args.input)
    except Exception as e:
        print('Error occured while reading the file: ', e)
        sys.exit(1)
        
    print('Running the job...')
    job(df)
    print(f'Complete. Check {args.output} for the output')
