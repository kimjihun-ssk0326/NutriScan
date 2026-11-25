# NutriScan Nutrition Dataset

NutriScan 프로젝트에서 사용하는 음식 영양정보 데이터입니다.

## Data Source

- **한글명:** 식품영양성분 데이터베이스
- **영문명:** Korean Food Composition Database system (K-FCDB)
- **제공기관:** 식품의약품안전처
- **원본 데이터:** 음식 DB (2026-08-28)
- **원본 데이터 수:** 19,617건
- **공식 사이트:** https://various.foodsafetykorea.go.kr/nutrient/

## Dataset Structure

| 파일 | 설명 |
|---|---|
| classes-v1.json | AI 음식 클래스와 food_id 매핑 |
| foods-v1.json | 음식별 영양정보 |
| manifests/ | 데이터 분할 및 관리 정보 |

## Nutrition Information

음식별 다음 정보를 관리합니다.

- 음식명 및 고유 ID
- 기준 제공량
- 칼로리(kcal)
- 탄수화물(g)
- 단백질(g)
- 지방(g)
- 데이터 출처

## Development Status

현재 음식 영양정보 데이터를 정리하고 있습니다.

AI 모델의 최종 음식 클래스가 확정되면 해당 음식의 영양정보를 선별하여 JSON 파일에 반영할 예정입니다.

## Attribution

본 프로젝트의 영양정보는 **식품영양성분 데이터베이스(K-FCDB)**를 출처로 사용합니다.

원본 데이터와 정제 데이터는 구분하여 관리합니다.