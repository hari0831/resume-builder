import pdfkit
from jinja2 import Environment, FileSystemLoader

def generate_pdf(data):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('resume_template.html')
    html_content = template.render(data=data)

    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    output_path = "resume.pdf"
    pdfkit.from_string(html_content, output_path, configuration=config)
    return output_path
