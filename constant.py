import pandas as pd


edu = [['BCA','CS','2019','MIMT KOTA (Raj)','68.23%'],['12th','Science','2016','RamganjMandi\'s ASSS', '70.40%'],['10th','-','2014','RamganjMandi\'s AVM','89.67%']]
info = {'name':'Jinendra Singh', 'Brief':'Dedicated Data Analyst with a strong foundation in Python, NumPy, Pandas, Data Visualization, and SQL. Passionate about extracting insights from data and contributing to data-driven decision-making. Seeking to leverage my skills and experience to deliver valuable analytical solutions.','photo':{'path':'abc.jpg','width':150}, 'Mobile':'7691094211','Email':'jinendrasingh0007@gmail.com','Medium':'https://medium.com/@jinendra-singh/about','City':'Kota, Rajasthan','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),'skills':['Data Science','SQL','Python','Streamlit', 'MS-EXCEL', 'HTML', 'CSS', 'C Language']}
blogs = {
         'link1': 'https://medium.com/@jinendra-singh/statistics-for-data-science-60c24d9423e9',
         'link2': 'https://medium.com/@jinendra-singh/probability-distribution-function-pdf-pmf-cdf-c9e91379615b',
         'link3': 'https://medium.com/@jinendra-singh/introduction-of-machine-learning-5fdf8c86b052',
         'link4': 'https://medium.com/@jinendra-singh/gradient-descent-from-scratch-ae8f2e309bb4',
         'link5': 'https://medium.com/@jinendra-singh/database-fundamentals-chepter-1-dfb3a7845551'
        }

skill_col_size = 5
embed_component = {'linkedin': """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge"
    data-locale="en_US"
    data-size="medium"
    data-theme="light"
    data-type="VERTICAL"
    data-vanity="jinendrasingh"
    data-version="v1">
    <a class="badge-base__link LI-simple-link"
        href="https://in.linkedin.com/in/jinendrasingh?trk=profile-badge">
    </a>
    <a href="https://in.linkedin.com/in/jinendrasingh?" target=_blank style="color:black;font-family:verdana;"> <b> Click here to check profile <b>
    </a>
</div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""}