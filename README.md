# NutriScan
AI-powered food image recognition and nutrition analysis service built on AWS

🍽️ NutriScan

AI-Powered Food Recognition & Nutrition Analysis

NutriScan은 음식 사진을 AI로 분석하여 음식 종류를 인식하고, 칼로리 및 영양정보를 제공하는 AWS 기반 웹 서비스입니다.

사용자는 음식 사진을 촬영하거나 업로드하여 분석 결과를 확인하고, 이전 분석 기록을 관리할 수 있습니다.

📌 한 장의 음식 사진으로 시작하는 간편한 영양정보 관리

📖 01. Project Overview

항목

내용

프로젝트명

NutriScan

프로젝트 유형

클라우드 컴퓨팅 학기 프로젝트

개발 인원

2명

플랫폼

모바일 웹 (Responsive Web)

AI 모델

MobileNetV3

클라우드

Amazon Web Services (AWS)

개발 방식

AI 모델 개발 + Serverless Architecture

현재 상태

개발 진행 중

🎯 Project Goals

음식 이미지 기반 AI 분류 모델 개발

한국 음식 중심의 이미지 데이터셋 구축

칼로리 및 주요 영양소 정보 제공

AWS 기반 서버리스 서비스 구현

사용자 분석 기록 저장 및 조회

모델 성능 평가 및 클라우드 운영 검증

✨ 02. Key Features

📸 Food Image Upload

음식 사진을 촬영하거나 선택하여 업로드합니다.

AWS S3 Presigned URL을 이용하여 이미지를 안전하게 저장합니다.

🤖 AI Food Recognition

MobileNetV3 기반 음식 이미지 분류 모델을 활용합니다.

SageMaker Endpoint에서 이미지 추론을 수행하고 음식 종류와 예측 신뢰도를 반환합니다.

🥗 Nutrition Analysis

예측된 음식 종류를 기반으로 영양정보 데이터베이스를 조회합니다.

제공 정보:

칼로리 (kcal)

탄수화물 (g)

단백질 (g)

지방 (g)

기준 제공량

※ 영양정보는 기준 제공량에 대한 참고값이며, 사진만으로 실제 섭취량을 정확하게 측정하는 기능은 포함하지 않습니다.

📋 Analysis History

사용자의 음식 분석 결과를 DynamoDB에 저장하고 이전 기록을 조회합니다.

🏗️ 03. System Architecture

NutriScan은 AWS 기반 서버리스 아키텍처를 사용하도록 설계되었습니다.

서비스 실행 흐름

User (Mobile Web)
       │
       ▼
Amazon API Gateway
       │
       ├── POST /uploads/presign
       │          │
       │          ▼
       │     Presign Lambda
       │          │
       │          ▼
       │     Presigned Upload URL
       │          │
       │          ▼
       │     User → Amazon S3
       │              (Direct Upload)
       │
       ├── POST /analyze
       │          │
       │          ▼
       │     Analyze Lambda
       │          │
       │          ├── Read Image from S3
       │          ├── Validate Image
       │          ├── SageMaker Endpoint
       │          ├── DynamoDB Nutrition Lookup
       │          └── Save Analysis History
       │
       └── GET /records
                  │
                  ▼
             Records Lambda
                  │
                  ▼
             Amazon DynamoDB

Architecture Components

AWS Service

역할

API Gateway

API 요청 라우팅

AWS Lambda

업로드 URL 발급, 분석 처리, 기록 조회

Amazon S3

음식 이미지 및 모델 파일 저장

Amazon SageMaker

음식 이미지 AI 추론

Amazon DynamoDB

음식 영양정보 및 분석 기록 저장

Amazon CloudWatch

로그 및 지표 모니터링

AWS IAM

서비스별 접근 권한 관리

🛠️ 04. Tech Stack

Frontend

React

TypeScript

HTML / CSS

Responsive Web Design

Backend

Python

AWS Lambda

Amazon API Gateway

Boto3

AI / Machine Learning

PyTorch

MobileNetV3

Transfer Learning

Google Colab

Amazon SageMaker

Cloud / Infrastructure

Amazon S3

Amazon DynamoDB

AWS IAM

Amazon CloudWatch

AWS SAM

Development Tools

Git / GitHub

Visual Studio Code

Claude Code

Impeccable

※ 기술 스택은 개발 계획을 포함하며, 모든 구성 요소의 구현 및 배포가 완료된 상태는 아닙니다.

📂 05. Project Structure

NutriScan/
│
├── frontend/               # 모바일 웹
│
├── backend/
│   ├── presign/            # S3 업로드 URL 발급
│   ├── analyze/            # 이미지 분석 및 영양정보 조회
│   └── records/            # 분석 기록 조회
│
├── ml/
│   ├── training/           # AI 모델 학습
│   ├── inference/          # SageMaker 추론 코드
│   └── evaluation/         # 모델 성능 평가
│
├── infra/                  # AWS 인프라 구성
├── docs/                   # 설계 및 개발 문서
│
├── README.md
└── PRODUCT.md

현재 기본 디렉터리 구조를 생성했으며, 세부 구현 파일은 개발 과정에서 추가할 예정입니다.

👥 06. Team & Responsibilities

팀원

담당 영역

주요 업무

김지훈

AI & Data

데이터셋 구축, MobileNetV3 학습·평가, 영양정보 데이터 구축

이서현

Cloud & Backend

AWS 아키텍처, Lambda API, S3·DynamoDB 연동, 배포 및 운영

공동

Frontend & Integration

웹 UI, 통합 테스트, GitHub 관리, 문서화

📊 07. Model Evaluation

모델의 성능을 정량적으로 평가하기 위해 다음 목표를 설정했습니다.

평가 지표

목표

Top-1 Accuracy

≥ 80%

Top-3 Accuracy

≥ 95%

Macro F1-score

≥ 0.75

분석 API 응답 시간

p95 ≤ 5초

※ 위 수치는 개발 목표이며, 실제 성능은 모델 학습 및 통합 테스트 후 공개할 예정입니다.

🚧 08. Development Status

Completed

GitHub 프로젝트 생성

프로젝트 기본 디렉터리 구성

팀원별 개발 역할 분담

AWS 아키텍처 설계 방향 수립

AI 모델 MobileNetV3 선정

In Progress / Planned

음식 이미지 데이터셋 구축

음식 클래스 및 영양정보 매핑

MobileNetV3 전이학습

모델 성능 평가

SageMaker Endpoint 배포

Lambda API 구현

DynamoDB 연동

모바일 웹 구현

전체 시스템 통합 테스트

운영 및 비용 검증

🔒 09. Security & Operations

NutriScan은 다음 보안 및 운영 원칙을 적용할 계획입니다.

IAM 최소 권한 원칙 적용

S3 버킷 비공개 설정

Presigned URL 기반 이미지 업로드

이미지 파일 형식 및 크기 검증

CloudWatch 기반 로그 및 오류 모니터링

AWS Budgets를 통한 비용 관리

테스트 종료 후 불필요한 AWS 자원 삭제

🚀 10. Getting Started

현재 프로젝트는 개발 초기 단계입니다.

추후 다음 내용을 추가할 예정입니다.

로컬 개발 환경 구성

Frontend 실행 방법

Lambda 테스트 방법

모델 학습 및 평가 방법

AWS SAM 배포 절차

API 사용 예시

📝 11. Project Documentation

프로젝트 개발 과정에서 다음 문서를 관리할 예정입니다.

PRODUCT.md — 프로젝트 요구사항 및 기능 범위

docs/architecture.md — 시스템 아키텍처

docs/openapi.yaml — API 명세

docs/deployment.md — 배포 및 자원 삭제 절차

NutriScan — Making Food Recognition Simple with AI & Cloud.