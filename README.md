# citizengalaxy.org

This is a research project which provides information on the galaxies and provides automated galaxy classification via a machine learning model such as Ec, Ei, Er, Sa, Sb, Sc, Sd, Se, SBa, SBb, SBc, SBd (Hubble Tuning Fork). 

## List of Minimal Software Tools Required & the Versions to Run
1. Python 3.10 or above
2. scikit-learn 1.4.2
3. Django Framework 4.2
4. DJango REST Framework 3.15.0
5. MySQL 8.0 Community Version

The above set of tools are minial to run the code on any environment.

## Setting up the Development Environment
The source shall be cloned from https://github.com/sujith-t/citizengalaxy Apart from the above software tools, following additional tools might aid development.
1. Git
2. Anaconda 24.1.0
3. Tensorflow 2.12
4. Jupyter Notebook 6.5.4
5. Postman API testing tool (any version)
6. JMeter (performance testing)

## Steps of Installation
First clone the source from the Git Repository. This requires a MySQL database available. The data for all the galaxies need to be imported to the database. The database dump and the Random Forest model file both are available. The database dump can be restored and the model file can be put inside /static folder. The file sizes prevents from committing to the Git Repository. If required pls contact s.thillayampalam@rgu.ac.uk Following are the steps of setting up.
1. Clone the code
2. Obtain MySQL dump and restore the database
3. Put the model file inside /static folder so that it could be loaded at the time of system startup
4. Change the database settings in /citizengalaxy/settings.py
5. Run the project by executing -> python ./manage.py runserver
6. Check on the browser http://localhost:8000
