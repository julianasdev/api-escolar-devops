from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, Base
from routers.alunos import alunos_router
from routers.cursos import cursos_router
from routers.matriculas import matriculas_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código a ser executado na inicialização
    print("Iniciando a aplicação e criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso. Aplicação pronta.")
    yield
    # Código a ser executado no encerramento (opcional)
    print("Encerrando a aplicação.")

app = FastAPI(
    title="API de Gestão Escolar", 
    description="""
        Esta API fornece endpoints para gerenciar alunos, cursos e turmas, em uma instituição de ensino.  
        
        Permite realizar diferentes operações em cada uma dessas entidades.
    """, 
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(alunos_router, tags=["alunos"])
app.include_router(cursos_router, tags=["cursos"])
app.include_router(matriculas_router, tags=["matriculas"])

@app.get("/")
def home():
    return {
        "mensagem": "API Escolar no ar! 🚀",
        "documentação": "/docs"
    }