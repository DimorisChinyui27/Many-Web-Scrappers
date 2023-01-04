from requests_html import HTML, HTMLSession
import csv

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Subject', 'Action', 'Add_Option'])
session = HTMLSession()
html_request = session.get("https://aitextpromptgenerator.com/builder?prompt=Kermit%20the%20frog%20muppet%20character%20jumping%20over%20a%20fence&rnd=1666185111347")
html_request.html.render(timeout=30)
#app= html_request.html.find('#app', first=True)
#item= app.find('.v-dialog__content v-dialog__content--active',first=True)
print(html_request.html)
