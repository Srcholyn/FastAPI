# Enter to folder
```
cd Web_app/frontend
cd Web_app/backend
```

# Enter to node cmd
```
FOR /f "tokens=*" %i IN ('fnm env --use-on-cd') DO CALL %i
```

# Run backend 
```
uvicorn main:app --reload
```
# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
