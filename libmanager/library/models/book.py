
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, ClassVar


@dataclass
class Book:
    """책 정보를 표현하는 데이터 클래스.
    TODO: 아래 요구사항을 만족하도록 구현을 보완하세요.
    - 인스턴스 변수: title(str), author(str), year(int)
    - 클래스 변수: book_count(int) — 생성될 때마다 +1
    - __str__는 "{title} by {author} ({year})" 형식 반환
    - @classmethod from_dict(cls, data: Dict[str, Any]) -> Book 구현
    """
    # 인스턴스 변수
    title: str
    author: str
    year: int
    
    # 클래스 변수
    book_count: ClassVar[int] = 0

    # book_count: int = 0  # 힌트: dataclass의 필드가 아닌 클래스 속성으로 선언
    def __post_init__(self):
        # 2. __init__ 대신 __post_init__을 사용합니다.
        # 이 메서드는 dataclass가 자동으로 __init__을 실행한 직후에 호출됩니다.
        Book.book_count += 1

    def __str__(self) -> str:
        # e.g. 책이름 by 지은이 (2001)
        str = f"{self.title} by {self.author} ({self.year})"
        return str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Book:
        return cls(
            title=data["title"],
            author=data["author"],
            year=data["year"]
        )