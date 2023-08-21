from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'company': "Unilever",
    'link': 'https://careers.unilever.com/job/-/-/34155/52218401040?utm_medium=job_posting&source=linkedin.com&utm_source=linkedin.com'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'company': 'CRED',
    'link':'https://www.linkedin.com/jobs/view/3691222064/?refId=c866c794-d9d0-4377-b3e6-2f7bd2afebb2&trackingId=i%2BPriCbiQk2SnlPVM9aRyQ%3D%3D'
  },
  {
    'id': 3,
    'title': 'Data Engineer 2',
    'location': 'Hyderabad, India',
    'company': 'Microsoft',
    'link':'https://jobs.careers.microsoft.com/us/en/job/1598715/Data-Engineer-II?jobsource=linkedin'
  },
  {
    'id': 4,
    'title': 'AI/ML Engineer',
    'location': 'Bengaluru, India',
    'company': 'Databricks',
    'link': 'https://www.databricks.com/company/careers/support/cloud-solutions-engineer-ai-ml-dev-6616027002?gh_jid=6616027002&gh_src=fd3a492b2us&source=LinkedIn'
  }
]



@app.route('/')
def hello():
    return render_template('home.html',
                           jobs = JOBS,
                           company_name = 'Sachendra')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)