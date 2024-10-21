
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
from playwright.async_api import async_playwright
import os

async def run_data(contest_id=1282,question_id="B1"):
    sub_id={}
    data=[]
    async with async_playwright() as p:
        id=os.getenv("id")
        password=os.getenv("pass")
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://codeforces.com/enter")

        await page.fill('#handleOrEmail',id)
        await page.fill('#password',password)
        await asyncio.sleep(5)
        await page.click('input.submit')

        for i in range(1,2):
            url=f"https://codeforces.com/contest/{contest_id}/status/{question_id}/page/{i}"
            await asyncio.sleep(5)
            await page.goto("http://codeforces.com")
            # await page.click('input[type="checkbox"]')
            await asyncio.sleep(5)
            response = await page.content()
            # print(response)
            soup = BeautifulSoup(response,"html.parser")
            print(soup)
            table_rows=soup.find('table',{'class':{'status-frame-datatable'}})
            print(table_rows)
            table_rows= soup.find_all('tr')
            for row in table_rows:
                columns = row.find_all('td')
                if columns:
                    data.append([columns[0].text.strip() for column in columns])

        await browser.close()
        print(data)
    return data

if __name__ == "__main__":
    asyncio.run(run_data())

