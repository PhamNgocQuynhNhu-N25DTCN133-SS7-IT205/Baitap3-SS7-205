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

