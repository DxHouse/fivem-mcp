#!/usr/bin/env node

const { spawn, execSync } = require("child_process");

function isCommandAvailable(cmd) {
  try {
    const checkCmd = process.platform === "win32" ? `where.exe ${cmd}` : `command -v ${cmd}`;
    execSync(checkCmd, { stdio: "ignore" });
    return true;
  } catch {
    return false;
  }
}

function printInstallInstructions() {
  console.error("\x1b[31m[fivem-mcp] Error: 'uv' is required to execute fivem-mcp.\x1b[0m\n");
  console.error("Please install 'uv' (fast Python package runner):\n");
  if (process.platform === "win32") {
    console.error("  \x1b[36mpowershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\"\x1b[0m\n");
  } else {
    console.error("  \x1b[36mcurl -LsSf https://astral.sh/uv/install.sh | sh\x1b[0m\n");
  }
  console.error("For more information, see: https://docs.astral.sh/uv/\n");
}

function main() {
  const hasUvx = isCommandAvailable("uvx");
  const hasUv = isCommandAvailable("uv");

  if (!hasUvx && !hasUv) {
    printInstallInstructions();
    process.exit(1);
  }

  const extraArgs = process.argv.slice(2);
  const cmd = hasUvx ? "uvx" : "uv";
  const baseArgs = hasUvx
    ? ["--from", "git+https://github.com/DxHouse/fivem-mcp", "fivem-mcp"]
    : ["tool", "run", "--from", "git+https://github.com/DxHouse/fivem-mcp", "fivem-mcp"];

  const child = spawn(cmd, [...baseArgs, ...extraArgs], {
    stdio: "inherit",
  });

  child.on("error", (err) => {
    console.error(`[fivem-mcp] Failed to launch server: ${err.message}`);
    process.exit(1);
  });

  child.on("close", (code) => {
    process.exit(code ?? 0);
  });
}

main();
