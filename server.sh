cd app/
# Start rasa server with nlu model
rasa run --model models --enable-api --cors "*" --debug \
          -p $PORT
		  
		  
cd app/
# Start rasa server with nlu model
rasa run actions --cors "*" --debug \
          -p $PORT
