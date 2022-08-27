
- development mode
```
DOT_ENV=development pipenv run start
```

- test mode
```
DOT_ENV=test pipenv run start
```


---

### 할당 문제

**배치를 주문 라인을 할당해야한다.**

`요구사항`
- 배치에는 재고가 있고 주문 라인에 x단위로 할당하면 가용 재고 수량은 x 만큼 줄어든다.
- 주문 라인에 할당된 재고 요청 이후 배치의 재고는 몇개 남을 것인가?
- 배치의 **가용 재고 수량** 과 주문 라인의 수량을 비교하여 주문 라인을 배치에 할당할 수 있는지 고려
- 같은 주문 라인을 두 번 이상 할당하면 안된다.
- 배치가 현재 배송 중이면 `ETA` 정보가 배치에 들어있다. `ETA`가 없는 배치는 창고 재고이다.
- 창고 재고를 배송 중인 배치보다 더 먼저 할당해야한다. 배송 중인 배치를 할당할 때는 ETA가 가장 빠른 배치를 먼저 할당한다.


1. Product
   - `sku` : 식별자 / 재고 유지단위
2. Customer
    - `order` : 주문을 발생시킨다.
3. Order
    - `orderid` : 주문 참조번호
    - `orderLine` : 하나 이상의 주문 라인 
4. OrderLine
    - `orderid` : 주문 참조번호
    - `sku` : 재고 유지단위
    - `qty` : 수량
    ex) `RED-CHAIR` 10단위
5. Batch
    - 구매 부서에서는 재고를 작은 `batch` 단위로 주문한다.
    - 재고 배치는 유일한 ID, SKU, QTY으로 이루어진다.

- Batch에 OrderLine을 할당해야하고 Batch에는 재고를 고객의 주소로 배송한다. Batch의 재고는 OrderLine의 가용 재고 수량을 갱신해야한다.
-   