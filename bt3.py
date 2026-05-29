# 1. PHÂN TÍCH INPUT / OUTPUT
# * Input: Chuỗi thô dữ liệu nhân sự (Kiểu dữ liệu: String), phân tách nhân viên bằng '|', phân tách thuộc tính bằng ';'. Lựa chọn menu và mã số ID cần tìm từ người dùng nhập vào (Kiểu dữ liệu: String).
# * Output: Menu tương tác, chuỗi dữ liệu gốc, hoặc bảng báo cáo nhân sự đã chuẩn hóa. Thông tin nhân viên tìm thấy theo ID hoặc thông báo lỗi nếu dữ liệu không hợp lệ.

# 2. ĐỀ XUẤT GIẢI PHÁP (HÀM & PHƯƠNG THỨC SỬ DỤNG)
# * Kiểm tra menu và số điện thoại hợp lệ: Dùng phương thức `.isdigit()` để kiểm tra ký tự số.
# * Tách dữ liệu: Dùng phương thức `.split('|')` để tách danh sách nhân viên và `.split(';')` để tách từng thuộc tính.
# * Làm sạch khoảng trắng: Dùng phương thức `.strip()` để loại bỏ toàn bộ khoảng trống thừa ở hai đầu chuỗi.
# * Định dạng chữ: Dùng phương thức `.upper()` cho ID và Phòng ban, dùng `.title()` cho Họ tên nhân viên.
# * Xử lý số điện thoại: Dùng `.replace('-', '')` xóa dấu gạch ngang, dùng kỹ thuật cắt chuỗi (Slicing) `[6:]` kết hợp toán tử cộng chuỗi với `"******"` để che số.
# * Căn lề báo cáo: Dùng các cú pháp định dạng F-string như `{biến:^độ_rộng}` để căn giữa và `{biến:<độ_rộng}` để căn trái.

# 3. THIẾT KẾ THUẬT TOÁN (LUỒNG CHƯƠNG TRÌNH)
# Bước 1: Khởi tạo biến dữ liệu thô `raw_data` và dùng vòng lặp `while True` hiển thị menu 4 chức năng.
# Bước 2: Nhận lựa chọn đầu vào của người dùng. Kiểm tra nếu nhập vào không phải là số hợp lệ hoặc nằm ngoài phạm vi từ 1 đến 4 thì thông báo lỗi và quay lại menu đầu tiên.
# Bước 3: Xử lý logic theo từng nhánh lựa chọn:
# Nhánh 1: In trực tiếp chuỗi dữ liệu `raw_data` gốc ra màn hình.
# Nhánh 2: Tách chuỗi thành danh sách nhân viên. Chạy vòng lặp `for` qua từng người, tách tiếp bằng dấu `;`. Áp dụng các phương thức làm sạch, định dạng chuỗi và kiểm tra định dạng số điện thoại như đề xuất. Sau đó in kết quả căn lề dạng bảng bằng F-string.
# Nhánh 3: Nhận mã ID cần tìm kiếm, làm sạch khoảng trắng và viết hoa bằng `.strip().upper()`. Chạy vòng lặp duyệt qua danh sách, chuẩn hóa ID của từng người để so sánh. Nếu trùng khớp thì in toàn bộ thông tin nhân viên đó ra và dừng vòng lặp bằng `break`. Nếu duyệt hết danh sách không tìm thấy mã phù hợp thì in thông báo "Không tìm thấy nhân viên".
# Nhánh 4: In thông báo "Thoát chương trình" ra màn hình và dùng lệnh `break` để dừng vòng lặp chính kết thúc ứng dụng.

raw_datam= ' eMP-001; nguyen van a ;098765432;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003; le van C ; 0988abc123 ; IT'
check = True

while check:
    print('\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====')
    print('1. Hiển thị chuỗi dữ liệu gốc')
    print('2. Chuẩn hóa dữ liệu và in báo cáo')
    print('3. Tìm kiếm nhân viên theo mã ID')
    print('4. Thoát chương trình')
    user = int(input('Nhập lựa chọn của bạn: '))

    match user:

        case 1:
            print(f'Chuỗi dữ liệu gốc:\n{raw_datam}')

        case 2:
            raw_datam.strip()
            customer_list = raw_datam.split('|')

            print("-" * 65)
            print(f"| {'ID':^10} | {'HỌ TÊN':<20} | {'SỐ ĐIỆN THOẠI':^15} | {'PHÒNG BAN':^10} |")
            print("-" * 65)

            for customer in customer_list:
                items = customer.split(';')

                customer_code = items[0].strip().upper()
                customer_name = items[1].strip().title()
                customer_company = items[3].strip().upper()
                customer_phone = items[2].strip().replace('-','')

                if customer_phone.isdigit():
                    after_phone = '******' + customer_phone[6:]
                else:
                    after_phone = 'Invalid Format'

                print(f"| {customer_code:^10} | {customer_name:<20} | {after_phone:^15} | {customer_company:^10} |")

            print("-" * 65)

        case 3:
            user_search = input('Nhập vào ID cần kiếm: ').strip().upper()

            found = False
            
            customer_list = raw_datam.split('|')

            for customer in customer_list:
                items = customer.split(';')

                customer_code = items[0].strip().upper()

                if customer_code == user_search:
                    customer_name = items[1].strip().title()
                    customer_company = items[3].strip().upper()
                    customer_phone = items[2].strip().replace('-','')
                
                    if customer_phone.isdigit():
                        after_phone = '******' + customer_phone[6:]
                    else:
                        after_phone = 'Invalid Format'
                
                    print("\n[ĐÃ TÌM THẤY NHÂN VIÊN]")
                    print(f" - Mã số: {customer_code}")
                    print(f" - Họ tên: {customer_name}")
                    print(f" - Số điện thoại: {after_phone}")
                    print(f" - Phòng ban: {customer_company}")

                    found = True
                    break
            if not found:
                print("Không tìm thấy nhân viên")

        case 4:
            print('Thoát chương trình...')
            break

