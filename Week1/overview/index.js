/* globals Tree */
'use strict';

var tree = new Tree(document.getElementById('tree'), {
  navigate: true // allow navigate with ArrowUp and ArrowDown
});
tree.on('open', e => console.log('open', e));
tree.on('select', e => console.log('select', e));
tree.on('action', e => console.log('action', e));
tree.on('fetch', e => console.log('fetch', e));
tree.on('browse', e => console.log('browse', e));

var structure = 
[
  {
    name: "Phân tích",
    open: false,
    type: Tree.FOLDER,
    selected: false,
    children:
    [
      {
        name: "Phân tích chức năng",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Xác định các tác nhân hệ thống (tác nhân là phần cứng, người sử dụng, cơ sở dữ liệu, hệ thống khác, ...)",
          },
          {
            name: "Vẽ biểu đổ use case tổng quan",
          },
          {
            name: "Vẽ biểu đồ use case phân rã (nếu cần)",
          },
          {
            name: "Vẽ biểu đồ hoạt động để biểu diễn quy trình nghiệp vụ",
          },
          {
            name: "Đặc tả ca use case, dùng use case descriptions",
          },
          {
            name: "Phân tích một số yêu cầu phi chức năng khác",
            open: false,
            type: Tree.FOLDER,
            selected: false,
            children:
            [
              {
                name: "Thời gian phản hồi (System-response time)",
              },
              {
                name: "Khả năng bảo trì và nâng cấp (Maintainability)",
              },
              {
                name: "Tính dễ dùng (Usability)",
              },
              {
                name: "Độ tin cậy (Reliability)",
              },
              {
                name: "Hiệu năng (Performance/Efficiency)"
              }
            ]
          },
          {
            name: "Ước tính: Phức tạp"
          }
        ]
      },
      {
        name: "Phân tích cấu trúc",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Thẻ CRC",
          },
          {
            name: "Vẽ biểu đồ lớp",
          },
          {
            name: "Ước tính: khá phức tạp"
          }
        ]
      },
      {
        name: "Phân tích hành vi",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Vẽ biểu đồ tuần tự (sequence diagram)",
          },
          {
            name: "Vẽ biểu đồ communication",
          },
          {
            name: "Note: Chỉ sử dụng một trong hai loại biểu đồ"
          },
          {
            name: "Ước tính: khá phức tạp"
          }
        ]
      }
    ]
  },
  {
    name: "Thiết kế",
    open: false,
    type: Tree.FOLDER,
    selected: false,
    children:
    [
      {
        name: "Thiết kế kiến trúc tổng thể của hệ thống",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Vẽ kiến trúc tổng quan của hệ thống, bao gồm các layers: front-end layer (giao diện người dùng), back-end layer (các xử lý nghiệp vụ của hệ thống), data layer (dữ liệu), có thể sử dụng mô hình MVC",
          },
          {
            name: "Ví dụ: Các thành phần của hệ thống bao gồm: client, web browser, server, database server"
          },
          {
            name: "Ước tính: rất đơn giản",
          }
        ]
      },
      {
        name: "Thiết kế chi tiết lớp",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Đặc tả chi tiết các lớp và các hàm",
            open: false,
            type: Tree.FOLDER,
            selected: false,
            children:
            [
              {
                name: "Review kết quả của pha phân tích, thêm các class, phương thức hay thuộc tính cần thiết cũng như bỏ đi những thứ dư thừa (nếu bước phân tích làm tốt thì bước này sẽ tốn ít công sức)",
              },
              {
                name: "Đặt chỉ định truy cập (public/private) cho các thuộc tính và phương thức của mỗi lớp",
              },
              {
                name: "Đặt chữ kí cho từng hàm: tên hàm, kiểu trả về, danh sách tham số",
              },
              {
                name: "Xác định các ràng buộc của mỗi phương thức, hoặc ràng buộc lên đối tượng của một lớp"
              },
              {
                name: "Xử lý ngoại lệ khi ràng buộc bị vi phạm"
              }
            ]
          },
          {
            name: "Xem xét khả năng sử dụng các frameworks, libraries để tăng tính tái sử dụng và giảm bớt công sức cần thực hiện"
          },
          {
            name: "Tái cấu trúc thiết kế",
            open: false,
            type: Tree.FOLDER,
            selected: false,
            children:
            [
              {
                name: "Phân rã các lớp phức tạp thành lớp con đơn giản hơn",
              },
              {
                name: "Chuẩn hóa (đối với các lớp sử dụng để lưu trữ dữ liệu trong cơ sở dữ liệu quan hệ)"
              }
            ]
          },
          {
            name: "Tối ưu thiết kế (tuning)",
            open: false,
            type: Tree.FOLDER,
            selected: false,
            children:
            [
              {
                name: "Đặt lại các thuộc tính trong các lớp (ví dụ: một thuộc tính f của class A có thể nên được đặt ở class B)"
              },
              {
                name: "Lưu các kết quả đã tính toán (có thể sử dụng biến hay thuộc tính) (caching computational results)"
              },
              {
                name: "Tối ưu đường đi của message giữa các objects (ví dụ: nếu message m đi từ object a đến object b thông phải đi qua một số object trung gian, có thể đặt một tham chiếu của b ở trong a để có message có thể đi trực tiếp từ a đến b)"
              },
            ]
          },
          {
            name: "Chuyển thiết kế các lớp từ tổng quát (không phụ thuộc ngôn ngữ lập trình) sang thiết kế cụ thể đối với ngôn ngữ lập trình"
          },
          {
            name: "Ước tính: phức tạp",
          }
        ]
      },
      {
        name: "Thiết kế giao diện",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Giao diện bên trong (internal interface)",
          },
          {
            name: "Giao diện bên ngoài (external interface)",
          },
          {
            name: "Giao diện người dùng (thường chỉ cần có thành phần này)",
          },
          {
            name: "Ước tính: trung bình"
          }
        ]
      },
      {
        name: "Thiết kế dữ liệu",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Vẽ sơ đồ thực thể liên kết",
          },
          {
            name: "Xác định các đối tượng và thông tin cần được lưu trữ trong cơ sở dữ liệu"
          },
          {
            name: "Xác định đặc điểm của dữ liệu (có cấu trúc hay phi cấu trúc)",
          },
          {
            name: "Lựa chọn định dạng lưu trữ",
            open: false,
            type: Tree.FOLDER,
            selected: false,
            children:
            [
              {
                name: "Tệp (tuần tự hoặc ngẫu nhiên)",
              },
              {
                name: "Cơ sở dữ liệu hướng đối tượng (object-oriented database)",
              },
              {
                name: "Cơ sở dữ liệu đối tượng - quan hệ (object-relational database)",
              },
              {
                name: "Cơ sở dữ liệu quan hệ (relational database)"
              }
            ]
          },
          {
            name: "Thiết kế các lớp truy cập và thao tác dữ liệu",
          },
          {
            name: "Ước tính: trung bình"
          }
        ]
      },
      {
        name: "Thiết kế kiến trúc tầng vật lý",
        open: false,
        type: Tree.FOLDER,
        selected: false,
        children:
        [
          {
            name: "Đặc tả phần cứng",
          },
          {
            name: "Đặc tả phần mềm",
          },
          {
            name: "Môi trường triển khai (ví dụ: môi trường mạng)",
          },
          {
            name: "Note: Phần thiết kế này thường được quy định bởi các yêu cầu phi chức năng",
          },
          {
            name: "Ước tính: đơn giản",
          }
        ]
      }
    ]
  }
];

// keep track of the original node objects
tree.on('created', (e, node) => {
  e.node = node;
});
tree.json(structure);