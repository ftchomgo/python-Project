def List_job(jenkins_url,jenkins_user,jenkins_pass):
    import jenkins
    jen_server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    user = jen_server.get_whoami()
    jobs = jen_server.get_jobs()

    Job_stats=[]
    for i in jobs:
        Job_name =i['name']
        Job_url = i['url'] 
        job_status= i['color']
        Job_stats.append([Job_name,Job_url,job_status])
    print(Job_stats)  
    return Job_stats
List_job("https://45.33.11.12:8080", "utrains", "devops")