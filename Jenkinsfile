pipeline {
    // 1. 指定执行环境
    // agent any 的意思是，让Jenkins随便找一台空闲的“工兵机”(Agent)来执行这个任务
    agent any

    // 2. 定义流水线的所有阶段
    stages {

        // 阶段一：检出代码 (Checkout)
        stage('Checkout Code') {
            steps {
                // 在真实的CI/CD环境中，这一步通常是 `git pull` 等命令，用来从代码仓库拉取最新代码
                // 由于我们是本地运行，代码已经存在，所以这里我们只打印一条信息来模拟这个过程
                sh 'echo "===== Simulating: Checking out latest code... ====="'
                sh 'ls -la' // 使用 `ls -la` 命令列出当前目录的所有文件，方便我们在日志中确认环境是否正确
            }
        }

        // 阶段二：构建Docker镜像 (Build Docker Image)
        stage('Build Docker Image') {
            steps {
                sh 'echo "===== Building the Docker image... ====="'
                // 执行我们已经非常熟悉的 docker build 命令
                sh 'docker build -t my-automation-project:latest .'
            }
        }

        // 阶段三：在Docker容器中运行测试 (Run Tests in Docker)
        stage('Run Automated Tests') {
            steps {
                sh 'echo "===== Running tests inside a Docker container... ====="'
                // 执行我们之前调试好的 docker run 命令
                // 注意：在真实的Jenkins Agent上，可能需要处理权限问题，但命令本身是一样的
                sh 'docker run --rm --network=host -v "$(pwd)/reports":/app/reports my-automation-project:latest'
            }
        }

        // 阶段四：归档和发布测试报告 (Archive Reports)
        stage('Publish Test Report') {
            steps {
                // 这一步使用的是Jenkins的一个插件(HTML Publisher)的功能
                // 它会在Jenkins的构建页面上，生成一个漂亮的链接，可以直接在线查看我们的HTML测试报告
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'test_report.html',
                    reportName: 'UI & API Test Report'
                ])
            }
        }
    }

    // 3. 定义流水线结束后的操作
    post {
        // `always` 表示无论流水线成功还是失败，这部分操作都会被执行
        always {
            echo '===== Pipeline finished. Cleaning up... ====='
            // 在这里，我们通常会加入清理工作，或者发送邮件/Slack通知等步骤
        }
    }
}
