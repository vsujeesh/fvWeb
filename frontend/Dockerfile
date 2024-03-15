FROM node:18 as build

WORKDIR /opt/fvweb/
COPY . .

RUN npm install
RUN npm run build

FROM nginx:alpine as prod

COPY --from=build /opt/fvweb/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
