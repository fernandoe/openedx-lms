FROM edxops/edxapp:latest

ADD ./edx-platform /edx/app/edxapp/edx-platform
ADD ./lms/hedu.py /edx/app/edxapp/edx-platform/lms/envs/hedu.py
ADD ./lms/hedu_test.py /edx/app/edxapp/edx-platform/lms/envs/hedu_test.py
ADD ./lms/hedu.py /edx/app/edxapp/edx-platform/cms/envs/hedu.py
ADD ./lms/hedu_test.py /edx/app/edxapp/edx-platform/cms/envs/hedu_test.py
ADD ./docker/run.sh /run.sh

RUN bash -c 'source /edx/app/edxapp/edxapp_env && cd /edx/app/edxapp/edx-platform && NO_PYTHON_UNINSTALL=1 paver install_prereqs'

RUN bash -c 'source /edx/app/edxapp/edxapp_env && cd /edx/app/edxapp/edx-platform && paver update_assets --settings hedu_test'

WORKDIR /edx/app/edxapp/edx-platform

CMD ["/run.sh"]
