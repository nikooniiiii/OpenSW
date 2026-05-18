from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
    <body>

        <h1>나의 첫 웹 페이지</h1>
        <p>FastAPI가 HTML을 반환했습니다.</p>

        <hr>

        <h2>나만의 질의응답기 with Local LLM</h2>
        <form action="/ask" method="post">
            <p>
                프롬프트: <input type="text" name="prompt" value="질문을 입력하세요">
            </p>
            <button type="submit">질문하기</button>
        </form>

        <hr>

        <h2>덧셈</h2>
        <form action="/add" method="get">
            <p>a: <input type="number" name="a" value="10"></p>
            <p>b: <input type="number" name="b" value="20"></p>
            <button type="submit">덧셈 실행</button>
        </form>

        <hr>

        <h2>뺄셈</h2>
        <form action="/minus" method="get">
            <p>a: <input type="number" name="a" value="10"></p>
            <p>b: <input type="number" name="b" value="20"></p>
            <button type="submit">뺄셈 실행</button>
        </form>

        <hr>

        <h2>사용자 등록</h2>
        <form action="/user" method="post">
            <p>이름: <input type="text" name="name" value="sdkim"></p>
            <p>나이: <input type="number" name="age" value="20"></p>
            <button type="submit">사용자 등록</button>
        </form>

    </body>
    </html>
    """

@router.get("/multi")
def multi(a: int, b: int):
return {"result": a * b}


@router.get("/subtract")
def subtract(a: int, b: int):
return {"result": a - b}


@router.post("/user")
def create_user(name: str = Form(...), age: int = Form(...)):
    return {
        "message": f"{name} 등록 완료",
        "age": age
    }