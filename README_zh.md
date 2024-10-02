# 科研项目组织框架

一个完整的科研项目涉及数据、代码和论文报告等多个方面，合理地组织这些内容有利于项目管理，便于复现、备份和留痕。  
这里结合实践经验，给出一套项目组织框架，灵感来源于 [Mario Krapp/semic-project](https://gitlab.pik-potsdam.de/krapp/semic-project) 和 [Joshua Cook](https://joshuacook.netlify.app/posts/2024-07-27_python-data-analysis-org/)。
利用 `cookiecutter` 工具，可以快速生成[如下所示的框架结构](#框架结构)，方便快速开始新的科研项目。

可以在[这里](https://mingzf.xyz/zh-cn/posts/%E9%A1%B9%E7%9B%AE%E7%BB%84%E7%BB%87/)查看更多关于我是如何利用这个组织框架开展科研项目的。

## 快速使用

```shell
pip install cookiecutter
cookiecutter https://github.com/Mingzefei/cookiecutter-science.git
```

## 框架结构

```text
.
├── AUTHORS.md                      <- 项目作者信息
├── LICENSE                         <- 项目使用的开源协议
├── README.md                       <- 项目的说明文件，包含项目介绍、安装说明等信息
├── backup                          <- 项目的备份文件夹，保存配置和结果等备份数据，不被版本控制追踪
├── config                          <- 配置文件存放目录
│   └── config.yaml                 <- 配置文件，包含计算参数和设置
├── data                            <- 项目使用的数据，不被版本控制追踪
│   ├── external                    <- 外部数据集，例如其他研究团队获取的验证或对比数据
│   ├── interim                     <- 中间数据，经过清洗、分组等初步处理，用于探索和后续步骤
│   ├── processed                   <- 最终处理后的数据集，用于建模和分析
│   └── raw                         <- 原始数据，未经任何处理
├── docs                            <- 项目的文档资料，包括技术文档和研究文献
├── notebooks                       <- 包含 Jupyter Notebook 文件，用于前期探索、代码实验与展示
│   └── 00_draft_example.ipynb      <- 示例 Notebook 文件，作为草稿
├── pyproject.toml                  <- 项目的配置文件，用于定义项目依赖、打包等设置
├── reports                         <- 学术报告和项目报告相关的内容
│   ├── Makefile                    <- 用于编译 LaTeX 报告的 Makefile 文件
│   ├── archive                     <- 归档的草稿
│   ├── figures                     <- 报告中的图表和图片
│   ├── main.tex                    <- 主报告的 LaTeX 源文件
│   └── si.tex                      <- 附加材料或补充信息的 LaTeX 文件
├── results                         <- 实验结果或分析结果的存储位置，不被版本控制追踪
├── scripts                         <- 各种可执行脚本，完成数据下载、清洗、备份等操作
│   ├── __init__.py                 <- 脚本模块初始化文件
│   ├── backup.py                   <- 数据备份脚本
│   ├── clean.py                    <- 数据清洗脚本
│   ├── config_loader.py            <- 配置文件加载脚本
│   ├── data_downloader.py          <- 数据下载脚本
│   └── paths.py                    <- 项目路径配置脚本，定义各文件夹路径
└── {{cookiecutter.project_slug}}   <- 项目核心代码（简称 src），可以独立打包成 Python package
    ├── __init__.py                 <- 项目包初始化文件
    ├── cli.py                      <- 命令行接口，用于调用项目核心功能
    ├── data                        <- 数据处理的逻辑函数
    │   ├── __init__.py             
    │   └── clean_data.py           <- 数据清洗的具体实现逻辑
    ├── external                    <- 外部的代码或库，不被版本控制追踪
    ├── models                      <- 模型构建和训练的代码
    │   └── __init__.py             
    ├── plot                        <- 数据可视化的逻辑代码
    │   ├── __init__.py             
    │   └── plot_style.py           <- 定义数据可视化风格和样式的脚本
    └── utils                       <- 工具类函数，包括文件读写、日志记录等辅助功能
        ├── __init__.py             
        ├── file_io.py              <- 文件输入输出处理逻辑
        └── logger.py               <- 日志记录逻辑
```

### 说明

（以下 `{{cookiecutter.project_slug}}` 简称为 `src`）

1. `src` 是核心代码，输入输出均为抽象的数据结构，不涉及具体的文件或路径；独立于项目其余内容，可以作为独立的 package 发布。
    - `src/data`：数据处理的逻辑函数。
    - `src/utils`：工具函数和辅助类，如文件读写、日志记录等。
    - `src/models`：模型构建的逻辑函数和类。
    - `src/plot`：可视化的逻辑函数和类。
2. `scripts` 主要包含可执行脚本，如数据下载、模型训练、结果备份等。这些脚本可以调用 `scripts/paths.py`、`scripts/config_loader.py` 和 `src`，以获取路径、配置和逻辑代码。
    - `scripts/paths.py`：项目的文件夹路径定义，用于指定输入输出，通常固定不变。
    - `scripts/config_loader.py`：项目的配置文件加载器，用于指定实验参数等，可根据需要修改。
3. `notebooks` 包含所有的 Jupyter Notebook 文件，早期用于快速构建代码和探索，后期用于执行和展示。
    - 建议定期将 `notebooks` 中的代码封装进 `src` 和 `scripts` 中，保持 notebook 文件的整洁，并便于项目自动化操作。
    - Jupyter Notebook 文件的命名格式为 `<递增编号>_<描述性名称>.ipynb`，如 `01_data_process.ipynb`。其中，`<递增编号>` 建议使用两位数字 `xy`，`y` 为递增数字，`x` 的取值含义如下：
        - 0：草稿
        - 1：数据
        - 2：模型
        - 3：结果（如可视化）
        - 4：报告
4. `docs` 用于存放项目的相关文献和技术文档。
5. `reports` 存放项目的最终学术报告（如 LaTeX 文件），以及归档的草稿文件（如 md、docx、pptx、pdf 等）。
6. `data` 存放项目使用的数据文件，通常体积较大，不受 git 版本控制管理。
    - `data/raw`：原始数据，从数据源下载，不应手动修改。
    - `data/interim`：中间数据，经过初步处理，可用于后续步骤。
    - `data/processed`：最终处理后数据，用于建模和分析。
    - `data/external`：外部研究团队的数据集，用于验证和比较。

此外，项目默认不会追踪以 `-private` 结尾的文件夹及其下内容，可用于存放私人文件。

## 未来可能会添加的特性

- code tests
- code format check
- continuous integration

## 文献资料

- 编写代码时的一些原则：[Guiding Design Principles](https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html#write-for-readability)（本项目的许多设计思路受此启发）
- 一些值得借鉴的 cookiecutter 模板
	- [NSLS-II/scientific-python-cookiecutter](https://github.com/NSLS-II/scientific-python-cookiecutter)
	- [jbusecke/cookiecutter-science-project](https://github.com/jbusecke/cookiecutter-science-project/tree/master)
