import asyncio
from pyppeteer import launch

async def is_handle_claimed(handle):
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    url = f"https://twitter.com/{handle}"
    await page.goto(url)
    
    # Wait for the page to finish loading
    await page.waitForNavigation()
    
    claimed = False
    if not await page.querySelector("div[data-testid='primaryColumn'] h2"):
        claimed = True

    await browser.close()
    return claimed

handle = "example_handle"
if asyncio.get_event_loop().run_until_complete(is_handle_claimed(handle)):
    print(f"The handle @{handle} is claimed.")
else:
    print(f"The handle @{handle} is not claimed.")