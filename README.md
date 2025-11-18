# 배달 앱 백엔드 시스템

Flask 기반의 배달 앱 백엔드 시스템입니다. 사용자(고객), 사장, 라이더 3가지 역할을 지원하는 배달 플랫폼입니다.

## 🚀 시작하기

### 방법 1: Docker로 실행 (권장)

Docker를 사용하면 MySQL과 웹 애플리케이션을 자동으로 설정하고 실행할 수 있습니다.

#### 필수 요구사항
- Docker Desktop 또는 Docker Engine
- Docker Compose

#### 설치 및 실행 방법

1. **저장소 클론 및 디렉토리 이동**
```bash
cd database
```

2. **환경 변수 설정**
`.env` 파일을 프로젝트 루트에 생성하고 다음 내용을 추가하세요:
```env
# 데이터베이스 설정
DB_HOST=localhost
DB_USER=root
DB_ROOT_PASSWD=your_root_password
DB_NAME=DeliveryBase
DB_PASSWD=your_password
```

3. **Docker 컨테이너 빌드 및 실행**
```bash
docker compose up --build
```

4. **애플리케이션 접속**
- 웹 애플리케이션: `http://localhost:5001`
- MySQL 데이터베이스: `localhost:3307` (외부 접속용)

> **참고**: 
> - 첫 실행 시 MySQL 컨테이너가 초기화되며 `create.sql`이 자동으로 실행됩니다.
> - 기본 데이터(지불방식 2개, 카테고리 6개)가 자동으로 삽입됩니다.
> - 컨테이너를 중지하려면 `Ctrl+C`를 누르거나 `docker compose down`을 실행하세요.
> - 컨테이너를 백그라운드에서 실행하려면 `docker compose up -d`를 사용하세요.

#### Docker 명령어
```bash
# 컨테이너 시작
docker compose up

# 컨테이너 시작 (백그라운드)
docker compose up -d

# 컨테이너 중지
docker compose down

# 컨테이너 재빌드 및 시작
docker compose up --build

# 로그 확인
docker compose logs -f

# 특정 서비스 로그 확인
docker compose logs -f web
docker compose logs -f db
```

---

### 방법 2: Docker 없이 실행

로컬 환경에서 직접 실행하는 방법입니다.

#### 필수 요구사항
- Python 3.8 이상
- MySQL 8.0 이상 (로컬에 설치되어 있어야 함)
- pip

#### 설치 및 실행 방법

1. **저장소 클론 및 디렉토리 이동**
```bash
cd database
```

2. **가상환경 생성 및 활성화**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **의존성 설치**
```bash
pip install -r requirements.txt
```

4. **MySQL 데이터베이스 생성**
MySQL에 접속하여 데이터베이스를 생성하세요:
```sql
CREATE DATABASE DeliveryBase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

또는 `create.sql` 파일을 직접 실행하세요:
```bash
mysql -u root -p < create.sql
```

5. **환경 변수 설정**
`.env` 파일을 프로젝트 루트에 생성하고 다음 내용을 추가하세요:
```env
SECRET_KEY=your-secret-key-here
DB_HOST=localhost
DB_USER=root
DB_PASSWD=your_password
DB_NAME=DeliveryBase
DB_PORT=3306
```

또는 비밀번호가 없는 경우:
```env
SECRET_KEY=your-secret-key-here
DB_HOST=localhost
DB_USER=root
DB_PASSWD=
DB_NAME=DeliveryBase
DB_PORT=3306
```

6. **애플리케이션 실행**
```bash
python app.py
```

서버가 `http://localhost:5001`에서 실행됩니다.

> **참고**: 애플리케이션 실행 시 데이터베이스와 테이블이 자동으로 생성되며, 기본 데이터(지불방식 2개, 카테고리 6개)가 자동으로 삽입됩니다.

## 📁 프로젝트 구조

```
database/
├── app.py                 # Flask 애플리케이션 메인 파일
├── config.py              # 데이터베이스 설정 파일
├── models.py              # SQLAlchemy 모델 정의
├── requirements.txt       # Python 패키지 의존성
├── create.sql            # 데이터베이스 스키마 및 기본 데이터
├── README.md             # 프로젝트 문서
├── FEATURES.md           # 기능 목록 문서
├── routes/               # 라우터 Blueprint
│   ├── __init__.py
│   ├── users.py          # 사용자 라우터
│   ├── owners.py         # 사장 라우터
│   ├── riders.py         # 라이더 라우터
│   ├── stores.py         # 가게 라우터
│   ├── customer.py       # 고객 라우터
│   ├── favorites.py      # 찜하기 라우터
│   ├── reviews.py        # 리뷰 라우터
│   ├── payments.py       # 결제수단 라우터
│   ├── coupons.py        # 쿠폰 라우터
│   └── admin.py          # 관리자 라우터
├── templates/            # Jinja2 템플릿
│   ├── firstpage.html    # 첫 페이지 (로그인/회원가입)
│   ├── signup.html       # 회원가입 페이지
│   ├── main.html         # 메인 페이지 (카테고리별 가게 목록)
│   ├── storelist2.html   # 가게 목록 페이지
│   ├── storedetail.html  # 가게 상세 페이지
│   ├── cart.html         # 장바구니 페이지
│   ├── order.html        # 주문 내역 페이지
│   ├── orderlist2.html   # 주문 목록 페이지
│   ├── like.html         # 찜 목록 페이지
│   ├── payment.html      # 결제 페이지
│   ├── owner.html        # 사장님 페이지
│   ├── rider.html        # 라이더 페이지
│   ├── setting.html      # 설정 페이지
│   └── admin.html        # 관리자 페이지
└── utils/                # 유틸리티 함수
    └── auth.py           # 인증 관련 함수 (login_required, owner_required 등)
```

## 📋 주요 기능

### 사용자 (User)
- 회원가입/로그인
- 사용자 정보 조회 및 수정
- 주소 수정
- 세션 기반 인증

### 사장 (Owner)
- 사장 회원가입/로그인
- 가게 등록 및 수정
- 메뉴 관리 (추가/삭제)
- 리뷰 조회 및 삭제
- **여러 지불방식 선택** (가게 설정 시)
- 카테고리 선택
- **쿠폰 관리** (추가/삭제, 할인 금액 및 유효기간 설정)

### 라이더 (Rider)
- 라이더 등록
- 라이더 정보 조회

### 고객 (Customer)
- **동적 카테고리 목록 조회** (데이터베이스에서 자동 로드)
- 카테고리별 가게 목록 조회
- 가게 상세 정보 조회 (평균 별점, 주문 수 표시)
- 메뉴 조회
- 장바구니 기능
- 주문 생성 및 조회
- 주문 내역 확인
- **리뷰 작성** (별점 선택 시 선택한 개수만큼만 표시)
- 찜하기 기능
- **쿠폰 적용** (할인 금액만 지원)
- **가게별 지불방식 선택** (가게에서 설정한 지불방식만 표시)

### 관리자 (Admin)
- **데이터베이스 관리 콘솔**
  - 각 항목별 목록 조회 (카테고리, 사용자, 가게, 메뉴, 쿠폰)
  - 각 항목별 개별 삭제
  - 테이블 형태로 데이터 표시
- 카테고리 관리 (생성, 삭제, 초기화)
- 사용자 관리 (생성, 삭제, 초기화)
- 가게 관리 (생성, 삭제, 초기화)
- 메뉴 관리 (생성, 삭제, 초기화)
- 쿠폰 관리 (생성, 삭제, 초기화)
- 테스트 데이터 생성 (seed)
- 전체 데이터 초기화

### 기타 기능
- 찜하기 (Favorite Store)
- 리뷰 작성 및 조회 (별점 시스템 개선)
- 지불방식 관리 (Payment)
- 쿠폰 관리 (Coupon) - 할인 금액만 지원
- 세션 유효성 검사 미들웨어
- **가게별 여러 지불방식 지원** (StorePayment 테이블)

## 🗄️ 데이터베이스 구조

### 기본 데이터
애플리케이션 실행 시 자동으로 삽입되는 기본 데이터:

**지불방식 (Payment)**
- 만나서 카드결제
- 만나서 현금 결제

**카테고리 (Category)**
- 한식
- 일식
- 중식
- 양식
- 분식
- 패스트푸드

### 주요 테이블
- `user` - 사용자 정보
- `owner` - 사장 정보
- `rider` - 라이더 정보
- `store` - 가게 정보
- `category` - 카테고리 정보
- `payment` - 지불방식 정보
- `store_payment` - 가게별 지불방식 (다대다 관계)
- `menu` - 메뉴 정보
- `order` - 주문 정보
- `review` - 리뷰 정보
- `favorite_store` - 찜하기 정보
- `coupon` - 쿠폰 정보 (할인 금액만 저장)

## 🔌 주요 API 엔드포인트

### 사용자 관련
- `POST /users/register` - 회원가입
- `POST /users/login` - 로그인
- `GET /users/me` - 현재 사용자 정보 조회
- `GET /users/setting` - 설정 페이지
- `POST /users/check-id` - 아이디 중복 확인

### 고객 관련
- `GET /customer/categories` - 카테고리 목록 (동적 로드)
- `GET /customer/categories/{category_id}/stores` - 카테고리별 가게 목록
- `GET /customer/stores/{store_id}` - 가게 상세 정보 (평균 별점, 주문 수 포함)
- `GET /customer/stores/{store_id}/menus` - 가게 메뉴 목록
- `GET /customer/stores/{store_id}/payments` - 가게 지불방식 목록 (여러 개)
- `GET /customer/stores/{store_id}/coupons` - 가게 쿠폰 목록
- `GET /customer/payment-methods` - 모든 지불방식 목록
- `POST /customer/orders` - 주문 생성
- `GET /customer/orders` - 주문 목록 조회

### 가게 관련
- `POST /stores/register` - 가게 등록 (여러 지불방식 선택 가능)
- `PUT /stores/{store_id}` - 가게 정보 수정 (여러 지불방식 선택 가능)
- `GET /stores/owner/{user_id}` - 사장별 가게 목록
- `GET /stores/{store_id}` - 가게 상세 정보 (평균 별점, 주문 수 계산)

### 찜하기 관련
- `POST /favorites` - 찜하기 추가
- `DELETE /favorites/{favorite_id}` - 찜하기 삭제
- `GET /favorites/page` - 찜 목록 페이지

### 리뷰 관련
- `POST /reviews` - 리뷰 작성 (별점 선택 개선)
- `GET /reviews/store/{store_id}` - 가게별 리뷰 목록
- `GET /reviews/order/{order_id}` - 주문별 리뷰 작성 페이지

### 쿠폰 관련
- `POST /coupons/store/{store_id}` - 쿠폰 생성 (할인 금액만)
- `GET /coupons/store/{store_id}` - 가게 쿠폰 목록
- `DELETE /coupons/{coupon_id}` - 쿠폰 삭제

### 관리자 관련
- `GET /admin/page` - 관리자 페이지
- `GET /admin/categories/list` - 카테고리 목록 조회
- `GET /admin/users/list` - 사용자 목록 조회
- `GET /admin/stores/list-all` - 가게 목록 조회
- `GET /admin/menus/list` - 메뉴 목록 조회
- `GET /admin/coupons/list` - 쿠폰 목록 조회
- `DELETE /admin/categories/{category_id}` - 카테고리 개별 삭제
- `DELETE /admin/users/{user_id}` - 사용자 개별 삭제
- `DELETE /admin/stores/{store_id}` - 가게 개별 삭제
- `DELETE /admin/menus/{menu_id}` - 메뉴 개별 삭제
- `DELETE /admin/coupons/{coupon_id}` - 쿠폰 개별 삭제
- `POST /admin/categories/create` - 카테고리 생성
- `POST /admin/users/create` - 사용자 생성
- `POST /admin/stores/create` - 가게 생성
- `POST /admin/menus/create` - 메뉴 생성
- `POST /admin/coupons/create` - 쿠폰 생성
- `POST /admin/categories/seed` - 카테고리 테스트 데이터 생성
- `POST /admin/users/seed` - 사용자 테스트 데이터 생성
- `POST /admin/stores/seed` - 가게 테스트 데이터 생성
- `POST /admin/menus/seed` - 메뉴 테스트 데이터 생성
- `POST /admin/coupons/seed` - 쿠폰 테스트 데이터 생성
- `DELETE /admin/categories/clear` - 카테고리 전체 삭제
- `DELETE /admin/users/clear` - 사용자 전체 삭제
- `DELETE /admin/stores/clear` - 가게 전체 삭제
- `DELETE /admin/menus/clear` - 메뉴 전체 삭제
- `DELETE /admin/coupons/clear` - 쿠폰 전체 삭제
- `POST /admin/reset` - 전체 데이터 초기화

## 🛠️ 기술 스택

- **프레임워크**: Flask 3.0.0
- **데이터베이스**: MySQL 8.0
- **ORM**: SQLAlchemy 2.0.44
- **템플릿 엔진**: Jinja2 3.1.2
- **인증**: Flask Session 기반
- **데이터베이스 드라이버**: PyMySQL 1.1.0
- **환경 변수 관리**: python-dotenv 1.0.0

## 🔒 보안 기능

- 세션 기반 인증
- 비밀번호 해싱 (Werkzeug)
- 세션 유효성 검사 미들웨어 (사용자/사장 삭제 시 자동 로그아웃)
- 로그인 필요 경로 보호 (`@login_required` 데코레이터)
- 사장 권한 검증 (`@owner_required` 데코레이터)
- 가게 소유권 검증

## 📝 주요 특징

1. **자동 데이터베이스 초기화**: 앱 실행 시 데이터베이스와 테이블이 자동으로 생성됩니다.
2. **기본 데이터 자동 삽입**: 지불방식 2개와 카테고리 6개가 자동으로 삽입됩니다.
3. **세션 유효성 검사**: 모든 요청 전에 세션의 사용자/사장 정보가 실제로 존재하는지 확인합니다.
4. **관리자 기능**: 웹 인터페이스를 통한 데이터 관리 및 테스트 데이터 생성 기능을 제공합니다.
5. **데이터베이스 관리 콘솔**: 각 항목별 목록 조회 및 개별 삭제가 가능한 관리 콘솔을 제공합니다.
6. **동적 카테고리 로드**: 메인 페이지에서 데이터베이스의 카테고리를 동적으로 로드하여 표시합니다.
7. **여러 지불방식 지원**: 가게별로 여러 지불방식을 설정할 수 있으며, 결제 시 가게에서 설정한 지불방식만 표시됩니다.
8. **쿠폰 시스템**: 할인 금액 기반 쿠폰 시스템 (할인율 미지원)
9. **리뷰 별점 시스템**: 별점 선택 시 선택한 개수만큼만 노란색으로 표시됩니다.
10. **가게 통계**: 가게 상세 정보에 평균 별점 및 주문 수가 표시됩니다.

## 🎨 UI/UX 개선사항

- **메인 페이지**: 카테고리를 데이터베이스에서 동적으로 로드하여 표시
- **리뷰 작성**: 별점 선택 시 선택한 개수만큼만 노란색으로 표시
- **결제 페이지**: 가게에서 설정한 지불방식만 라디오 버튼으로 표시
- **가게 상세**: 평균 별점 및 주문 수 표시
- **관리자 페이지**: 데이터베이스 관리 콘솔 형태로 각 항목별 목록 조회 및 개별 삭제 가능

## 🐛 문제 해결

### Docker 관련 문제

#### 데이터베이스 연결 실패 (Docker)
- 컨테이너가 정상적으로 실행 중인지 확인하세요: `docker compose ps`
- `.env` 파일의 `DB_HOST=db`, `DB_USER=root`, `DB_PASSWD`, `DB_NAME=DeliveryBase`가 올바른지 확인하세요.
- MySQL 컨테이너 로그 확인: `docker compose logs db`
- 웹 컨테이너 로그 확인: `docker compose logs web`
- 컨테이너를 재시작해보세요: `docker compose restart`

#### 포트 충돌 (Docker)
- 기본 포트는 5001입니다. 다른 포트를 사용하려면 `docker-compose.yml`의 `ports` 섹션을 수정하세요.
- 포트가 이미 사용 중인 경우: `docker compose down` 후 다른 포트로 변경하세요.

#### 컨테이너가 시작되지 않을 때
- Docker Desktop이 실행 중인지 확인하세요.
- 컨테이너를 완전히 제거하고 다시 시작: `docker compose down -v && docker compose up --build`
- 볼륨을 삭제하고 초기화: `docker volume rm database_db_data`

### 로컬 실행 관련 문제

#### 데이터베이스 연결 실패 (로컬)
- MySQL 서버가 실행 중인지 확인하세요.
- `.env` 파일의 `DB_HOST=localhost`, `DB_USER=root`, `DB_PASSWD`, `DB_NAME=DeliveryBase`가 올바른지 확인하세요.
- 데이터베이스가 생성되어 있는지 확인하세요: `mysql -u root -p -e "SHOW DATABASES;"`
- MySQL 포트가 3306인지 확인하세요.

#### 포트 충돌 (로컬)
- 기본 포트는 5001입니다. 다른 포트를 사용하려면 환경 변수 `PORT`를 설정하세요.
- 포트가 이미 사용 중인 경우: `lsof -i :5001`로 프로세스를 확인하고 종료하세요.

### 공통 문제

#### 기본 데이터가 없을 때
- 앱을 재시작하면 자동으로 기본 데이터가 삽입됩니다.
- 또는 관리자 페이지에서 수동으로 데이터를 생성할 수 있습니다.

#### 관리자 페이지 접근
- 관리자 페이지는 `/admin/page`에서 접근할 수 있습니다.
- 로그인 정보: 아이디 `root`, 비밀번호 `root`

#### 테이블이 생성되지 않을 때
- 데이터베이스 연결이 정상인지 확인하세요.
- `create.sql` 파일이 올바른지 확인하세요.
- 로그에서 에러 메시지를 확인하세요.

## 📄 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.
