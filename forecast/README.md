Chỉ số đánh giá cho mô hình là **MAPE** (The mean absolute percentage error) là một thước đo thống kê về mức độ chính xác của hệ thống dự báo. Nó đo lường độ chính xác này dưới dạng phần trăm và có thể được tính bằng sai số phần trăm tuyệt đối trung bình tại mỗi bước thời gian giữa giá trị thực tế và giá trị dự báo chia cho các giá trị thực tế theo công thức:$$\text{M}=\frac{1}{n}\sum^n_{t=1}\left|\frac{A_t-F_t}{A_t}\right|$$ 
>- $A_t$: giá trị thực
>- $F_t$: giá trị dự báo
>- $n$: số lượng observations.

Sai số phần trăm tuyệt đối trung bình (MAPE) là thước đo phổ biến nhất được sử dụng để dự báo lỗi và hoạt động tốt nhất nếu dữ liệu không có giá trị extremes (và không có giá trị 0).

*source: [DataScienceWorld, TowardDS-Staff. (2021). Viet Nam Stock Market Prediction . Kaggle](https://www.kaggle.com/competitions/stock-market-prediction)