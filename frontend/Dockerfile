FROM node:23-alpine3.20 

# Устанавливаем рабочую директорию  
WORKDIR /frontend  

COPY package*.json ./  

RUN npm install  

COPY . .  

RUN npm run build  
 