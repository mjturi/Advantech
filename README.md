# Advantech Development

## Some of the scripts I have written for data collection, data cleaning/merging, and recruiting

### Data Collection
- Script to search through booz allen website and save their company employee information to a csv. 
   - *bah_website_scrape.py*
- Script to hunt linkedin using a backend search query (provided) and save the employees’ names, titles, about paragraphs, desired company experience, and locations. <br>
   - *company_scrape_linkedin.py*<br>
   - Have hunted through: 
      - BAH NAVY, ARMY, USAF 
      - Leidos NAVY, ARMY, USAF 
      - Dynetics NAVY, ARMY, USAF 
- Script to hunt through google using filetype: *** query.
   - *doc_search.py*

### Data Cleaning
- Wrote a single script to sequentially: 
   - Split the data into corresponding fields of master spreadsheet 
   - Clean – drop duplicates, drop misc. Info that is irrelevant and wrong, populate expertise field 
   - Merge with the master spreadsheet, double check for dups, and output new master file 
- This sequence was executed each time that new data needed to be entered into a master sheet 
   - *data_merge.py*

### Govwin
- Wrote two scripts to scrape through govwin opportunities (saved or unsaved) and dive into attached documents for each opportunity. If an attachment posted matched something in or “keyword list”, the script downloads the file to the pc in a folder with the OP ID as the title 
   - *govwinscrape_nonsaved_opps.py*
   - *govwinscrape_saved_opps.py*
- Wrote a script to parse through govwin opportunities in San Diego with Leidos as incumbent (these can both be changed) and flag them to saved opportunities if they fell within a certain date range  
   - *govwin_flag_ops.py*

### LinkedIn
- Script to add new connections with a personalized connect message. The script executes a login to a LinkedIn profile, performs a backend LinkedIn query with given criteria, and will go through each person (up to a specified end), grab their names, and send a personalized connection message. 
   - *new_con_v1.py*
- Second script as a sort of follow-up to the previous one. New personalized message, better fielding criteria to yield narrower results within a company and attached website and other interesting links in message.  
    - *new_con_v2.py*
   - Both scripts were executed with various BAH criteria 
- Script to filter through existing LinkedIn connections (with changeable criteria), and invite them to follow the Advantech LI page 
   - *page_con.py*
   - Used BAH criteria
