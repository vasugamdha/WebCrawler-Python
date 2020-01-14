import threading
from queue import Queue
from spider import Spider
from domain import *
from start import *

PROJECT_NAME= 'Project_site'
HOMEPAGE = 'http://mldag.charusat.ac.in' #Enter your url here
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt' #list of urls to be crawled
CRAWLED_FILE =  PROJECT_NAME + '/crawled.txt' #list of urls crawled
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' Links in the queue ')
        create_jobs()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon=True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

create_workers() # starts threading
crawl()# main crawler starts from here




