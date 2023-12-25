from multiprocessing import Pool
from tqdm import tqdm
import pandas as pd
from Link_Scraper import process_website
from Parsing import processing_links

from selenium.webdriver.common.action_chains import ActionChains



if __name__ == '__main__':
    links = process_website()

    with Pool(processes=15) as pool, tqdm(total=len(links), desc="Parsing...") as pbar:
        results = []
        for result in pool.imap_unordered(processing_links, links):
            if result is not None:
                pbar.update()
                results.append(result)



    df = pd.DataFrame(results)
    df.to_csv('corpus_usa.csv', index=False, encoding='utf-8')






