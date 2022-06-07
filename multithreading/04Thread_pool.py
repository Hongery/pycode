from concurrent.futures import ThreadPoolExecutor, as_completed
import blog_spider

# craw
with ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
with ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # 顺序
    for future, url in futures:
        print(url, future.result())

    for future in as_completed(futures):
        url = futures[future]
        print(url, future.result())
