from pydantic import BaseModel
from datetime import datetime

# Add this model in main.py
class VisitorLog(BaseModel):
    name: str
    visitor_type: str

@app.post("/api/visitor")
def log_visitor(visitor: VisitorLog):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO visitors (name, visitor_type) VALUES (%s, %s)"
        cursor.execute(query, (visitor.name, visitor.visitor_type))
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "success", "message": "Visitor logged successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
