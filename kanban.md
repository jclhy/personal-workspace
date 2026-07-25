# 全量任务看板数据

```javascript
const SECTIONS = [
  { cat:"E", title:"消耗型任务", subtitle:"必须做，优先清掉", icon:"🔥", color:"#c41e3a" },
  { cat:"C", title:"建设型·内容资产", subtitle:"长期价值最高", icon:"📚", color:"#ff9500" },
  { cat:"T", title:"建设型·技术项目", subtitle:"产品与技术", icon:"⚙️", color:"#2557a7" },
  { cat:"ED", title:"建设型·教育业务", subtitle:"教育产品与合作", icon:"🎓", color:"#34c759" },
  { cat:"B", title:"建设型·商业变现", subtitle:"收入与客户", icon:"💰", color:"#af52de" },
  { cat:"D", title:"已完成/维持型", subtitle:"保持运行即可", icon:"✅", color:"#8e8e93" },
  { cat:"L", title:"个人成长/学习", subtitle:"基础与支撑", icon:"🌱", color:"#5ac8fa" },
];

const STATUS_MAP = { "✅":"completed", "⏳":"inprogress", "🔴":"pending", "❌":"notstarted", "⏸️":"paused", "⚠️":"deferred" };
```

```javascript
const DEV_PROJECTS = [
  { id:"DEV-01", cat:"DEV", title:"LLM Gateway (API-Worlds)", status:"✅", statusLabel:"初版完成", env:"开发环境待定", tool:"—",
    desc:"统一聚合40+大模型API，OpenAI兼容接口。Python/FastAPI/SQLite/Gradio",
    details:{GitHub:"https://github.com/jclhy/API-Worlds"} },
  { id:"DEV-02", cat:"DEV", title:"DeepWork 个人工作平台（含日历+看板）",
    desc:"个人工作日历 + 全量看板 + 话题列表等。汉化+安全加固。",
    details:{GitHub:"https://github.com/jclhy/personal-workspace", 看板:"kanban.html GitHub Pages"},
    status:"✅", statusLabel:"已部署", env:"Home电脑 (DESKTOP-N463Q6P)", tool:"WorkBuddy" },
  { id:"DEV-03", cat:"DEV", title:"WinClaw 日常话题讨论",
    desc:"用于日常话题讨论、Agent协作。",
    details:{},
    status:"🔄", statusLabel:"进行中", env:"Home电脑 (DESKTOP-N463Q6P)", tool:"WinClaw" },
  { id:"DEV-04", cat:"DEV", title:"海东市就业服务数智化平台",
    desc:"9大系统35个子模块需求分析+报价方案，首年预算约6620万~12883万",
    details:{类型:"报价分析", 状态:"待用户确认细化方向"},
    status:"✅", statusLabel:"报价方案已完成", env:"云端 (Coze)", tool:"扣子/Excel Master Skill" },
  { id:"DEV-05", cat:"DEV", title:"FC 模拟平台",
    desc:"待实现网络共享卡带功能。",
    details:{},
    status:"⏳", statusLabel:"基础功能完成", env:"Home电脑 (DESKTOP-N463Q6P)", tool:"QoderWorkCn" },
  { id:"DEV-06", cat:"DEV", title:"电子交互教具（九识）",
    desc:"ESP32→GPIO→树莓派上位机，技术路线验证中。",
    details:{},
    status:"⏳", statusLabel:"模拟阶段", env:"Home电脑 (DESKTOP-N463Q6P)", tool:"WorkBuddy" },
];
```

```javascript
const TASKS = [
  // === 消耗型 E ===
  { id:"E-02", cat:"E", title:"青基会发票整理-禅城区", status:"⏳", statusLabel:"部分完成", priority:"P1", owner:"小森",
    desc:"佛山禅城区站发票整理已启动，部分票据已核实归档。参照肇庆站模板推进。",
    details:{来源:"飞书/小哲", 关联飞书:"—"} },
  { id:"E-03", cat:"E", title:"青基会发票整理-清远", status:"🔴", statusLabel:"刚开始", priority:"P1", owner:"小森",
    desc:"清远站发票整理刚启动。收集全部票据→逐张核实→按基金会格式提交。",
    details:{来源:"飞书/小哲", 关联飞书:"—"} },
  { id:"E-04", cat:"E", title:"青基会发票整理-山东站", status:"🔴", statusLabel:"未开始", priority:"P1", owner:"小森",
    desc:"山东站发票尚未开始整理。需先收集教师报名信息表和省青基会盖章名单（E-10前置）。",
    details:{来源:"飞书/小哲", 关联飞书:"NO.010"} },
  { id:"E-05", cat:"E", title:"青基会发票整理-广东站", status:"🔴", statusLabel:"未开始", priority:"P1", owner:"小森",
    desc:"广东站发票尚未开始整理。",
    details:{来源:"飞书/小哲", 关联飞书:"—"} },
  { id:"E-06", cat:"E", title:"公司垫付报销整理", status:"🔴", statusLabel:"待整理", priority:"P1", owner:"小森",
    desc:"个人垫付的公司费用需整理报销，与青基会发票分开走流程，两条线独立推进。",
    details:{来源:"小哲", 关联飞书:"—"} },
  { id:"E-07", cat:"E", title:"NO.020 梳理科技领航计划决算和报销", status:"⏳", statusLabel:"进行中", priority:"P1", owner:"小森",
    desc:"对科教领航计划进行全流程决算梳理。按站点逐一推进：肇庆→佛山→清远→淄博→增城。与E-01至E-05有交叉。",
    details:{来源:"飞书", 关联飞书:"NO.020"} },
  { id:"E-08", cat:"E", title:"NO.038 整理各阶段报销费用清单", status:"🔴", statusLabel:"待处理", priority:"P1", owner:"小森",
    desc:"整理山东站、广东站、英德站等各项目阶段报销费用明细，形成完整清单。",
    details:{来源:"飞书", 关联飞书:"NO.038"} },
  { id:"E-09", cat:"E", title:"NO.001 丁教授团队交通费报销", status:"🔴", statusLabel:"待处理", priority:"P1", owner:"小森",
    desc:"山师丁教授团队交通费报销。前置NO.036已完成（丁教授不报出租车费），障碍已解除可推进。属于科教领航计划山东站一部分。",
    details:{来源:"飞书", 关联飞书:"NO.001"} },
  { id:"E-10", cat:"E", title:"NO.010 山东站收集教师报名信息", status:"🔴", statusLabel:"待处理", priority:"P1", owner:"小森",
    desc:"收集山东站教师报名信息表和省青基会盖章教师名单。是E-04发票整理的前置材料。",
    details:{来源:"飞书", 关联飞书:"NO.010"} },

  // === 建设型 C · 内容资产 ===
  { id:"C-01", cat:"C", title:"《AI时代的成长力量》三本书（学生/家长/老师版）", status:"⏳", statusLabel:"已完成出版", priority:"P3", owner:"红业",
    desc:"独立编写，版权完全归属个人。学校无运营计划，跑通商业路径后可反哺公司。",
    details:{版权:"个人", 出版社:"—"} },
  { id:"C-02", cat:"C", title:"科普教育活动案例库", status:"🔄", statusLabel:"持续积累中", priority:"P2", owner:"红业",
    desc:"历次科普活动策划执行沉淀的案例、方案、素材，形成可复用资产。",
    details:{来源:"项目实践"} },

  // === 建设型 T · 技术项目 ===
  { id:"T-03", cat:"T", title:"电子交互教具", status:"⏳", statusLabel:"和Jay合作Dell有初步工作", priority:"P2", owner:"小民",
    desc:"基于地平线飞行器平台验证电子交互教具。技术路线：ESP32→蓝牙/WiFi+GPIO驱动→树莓派做上位机/学生终端。当前模拟阶段。下一步深入测试→公司现场复用。",
    details:{来源:"小哲", 话题编号:"—", 工具:"WorkBuddy", 环境:"Home电脑 (DESKTOP-N463Q6P)", 关联:"MEMORY.md状态锚点"} },
  { id:"T-04", cat:"T", title:"STEM教育平台", status:"⏸️", statusLabel:"原型完成已暂停", priority:"P3", owner:"小民",
    desc:"STEM/PBL教育平台原型已完成，当前暂停。技术方向待定。",
    details:{来源:"—", 话题编号:"—", 工具:"—"} },
  { id:"T-05", cat:"T", title:"话题管理工具链", status:"⏳", statusLabel:"持续维护中", priority:"P2", owner:"小森",
    desc:"话题管理、追踪、定期简报的自动化体系。包含话题清单、知识库同步等。",
    details:{来源:"自建", 话题编号:"—", 工具:"Coze Agent/飞书CLI", 环境:"云端"} },

  // === 建设型 ED · 教育业务 ===
  { id:"ED-01", cat:"ED", title:"科教领航计划后续站点收尾", status:"⏳", statusLabel:"进行中", priority:"P1", owner:"小森",
    desc:"科教领航计划各站点收尾工作：发票整理、报销、决算。与E-02至E-10交叉推进。",
    details:{来源:"飞书", 话题编号:"—" } },
  { id:"ED-02", cat:"ED", title:"科学家精神相关内容开发", status:"⏳", statusLabel:"持续推进", priority:"P2", owner:"红业",
    desc:"科学家精神主题的课程、活动、宣传内容开发与交付。",
    details:{来源:"项目需求"} },

  // === 建设型 B · 商业变现 ===
  { id:"B-01", cat:"B", title:"教育信息化平台商业化", status:"⏳", statusLabel:"探索中", priority:"P2", owner:"红业",
    desc:"基于现有教育信息化平台能力，探索商业化路径。",
    details:{来源:"自我评估"} },
  { id:"B-02", cat:"B", title:"科技教育副业拓展", status:"🔴", statusLabel:"规划阶段", priority:"P2", owner:"红业",
    desc:"利用20余年教育行业经验，拓展科技教育、科普活动相关的副业机会。注意：每周副业8-10小时上限。",
    details:{来源:"自我评估"} },

  // === 已完成/维持型 D ===
  { id:"D-01", cat:"D", title:"NO.030 英德站付款", status:"✅", statusLabel:"已完成", priority:"P1", owner:"小森",
    desc:"英德站付款流程已完成确认。",
    details:{来源:"飞书", 关联飞书:"NO.030"} },
  { id:"D-02", cat:"D", title:"NO.039 某站点结项", status:"✅", statusLabel:"已完成", priority:"P2", owner:"小森",
    desc:"某站点结项流程已完成。",
    details:{来源:"飞书", 关联飞书:"NO.039"} },
  { id:"D-03", cat:"D", title:"NO.043 等待NO.042完成后推进", status:"⏸️", statusLabel:"暂停", priority:"P2", owner:"小森",
    desc:"NO.043需等待NO.042完成后推进。",
    details:{来源:"飞书", 关联飞书:"NO.043"} },

  // === 个人成长/学习 L ===
  { id:"L-01", cat:"L", title:"中医保守治疗健康管理", status:"⏳", statusLabel:"持续中", priority:"P0", owner:"红业",
    desc:"右颞叶海马区低级别胶质瘤中医保守治疗，每3个月复查。2026年4月影像无进展，下次复查2026年7-8月杭州明州医院。",
    details:{医院:"杭州明州医院", 复查周期:"3个月"} },
  { id:"L-02", cat:"L", title:"编程能力提升", status:"⏳", statusLabel:"持续学习中", priority:"P2", owner:"红业",
    desc:"计算机专业背景，持续提升编程和系统架构能力。",
    details:{工具:"Coze CLI/Python/Bash"} },
  { id:"L-03", cat:"L", title:"个人工作操作系统优化", status:"⏳", statusLabel:"持续迭代", priority:"P2", owner:"小森",
    desc:"个人工作日历+看板+话题追踪一体化系统。健康底线：每周8-10小时副业上限，晚10点后不工作。",
    details:{工具:"Coze Agent/飞书CLI/Markdown", 环境:"云端+Home电脑"} },
];
```
