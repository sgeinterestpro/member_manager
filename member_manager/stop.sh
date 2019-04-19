ps -fu $USER|grep web_socket|grep -v grep |awk '{print $2}' | xargs kill -9
