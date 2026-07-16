def test_open_page(page):
     page.goto("https://testautomationpractice.blogspot.com/")
     print(f"Page title: {page.title()}")