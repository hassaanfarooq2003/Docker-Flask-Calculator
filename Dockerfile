# --------------------------- stage 1 -----------------
    FROM python:3.9-slim AS backend-build
    WORKDIR /app
    
    COPY ./app.py /app
    COPY ./requirements.txt /app
    
    RUN pip install --no-cache-dir -r requirements.txt
    # --------------------------- end of stage 1 -----------------

    # --------------------------- stage 2 -----------------
        
    FROM python:3.9-slim
    
    WORKDIR /app
    
    # Copy the installed dependencies from the previous stage
    COPY --from=backend-build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
    
    # Copy code from the previous stage
    COPY --from=backend-build /app /app
    
    RUN useradd -m localuser
    USER localuser
    
    EXPOSE 5000
    
    CMD ["python","app.py"]


    # --------------------------- end of stage 2 -----------------