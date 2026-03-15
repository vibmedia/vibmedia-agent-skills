# Architecture Map

```mermaid
graph TD
  root[".agent"]
  _shared[".shared"]
  _shared_ui_ux_pro_max["ui-ux-pro-max"]
  agents["agents"]
  brands["brands"]
  brands__industry_template["_industry-template"]
  brands__template["_template"]
  brands_accounting["accounting"]
  brands_travel["travel"]
  docs["docs"]
  mcp_servers["mcp-servers"]
  profiles["profiles"]
  rules["rules"]
  scripts["scripts"]
  scripts_auto_preview_py["auto_preview.py"]
  scripts_checklist_py["checklist.py"]
  scripts_session_manager_py["session_manager.py"]
  scripts_verify_all_py["verify_all.py"]
  scripts_verify_boundary_py["verify_boundary.py"]
  scripts_wordpress_checklist_py["wordpress_checklist.py"]
  skills["skills"]
  skills_ab_test_setup["ab-test-setup"]
  skills_ad_creative["ad-creative"]
  skills_ai_seo["ai-seo"]
  skills_analytics_tracking["analytics-tracking"]
  skills_api_patterns["api-patterns"]
  skills_app_builder["app-builder"]
  skills_architecture["architecture"]
  skills_architecture_explorer["architecture-explorer"]
  skills_bash_linux["bash-linux"]
  skills_behavioral_modes["behavioral-modes"]
  skills_brainstorming["brainstorming"]
  skills_business_listing["business-listing"]
  skills_churn_prevention["churn-prevention"]
  skills_clean_code["clean-code"]
  skills_client_communication["client-communication"]
  skills_cloud_infrastructure["cloud-infrastructure"]
  skills_code_review_checklist["code-review-checklist"]
  skills_cold_email["cold-email"]
  skills_competitor_alternatives["competitor-alternatives"]
  skills_composition_patterns["composition-patterns"]
  skills_content_strategy["content-strategy"]
  skills_copy_editing["copy-editing"]
  skills_copywriting["copywriting"]
  skills_data_analysis["data-analysis"]
  skills_database_design["database-design"]
  skills_deployment_procedures["deployment-procedures"]
  skills_design_system_architecture["design-system-architecture"]
  skills_documentation_templates["documentation-templates"]
  skills_email_sequence["email-sequence"]
  skills_envato_template_selection["envato-template-selection"]
  skills_executing_plans["executing-plans"]
  skills_finishing_a_development_branch["finishing-a-development-branch"]
  skills_form_cro["form-cro"]
  skills_free_tool_strategy["free-tool-strategy"]
  skills_frontend_design["frontend-design"]
  skills_game_development["game-development"]
  skills_geo_fundamentals["geo-fundamentals"]
  skills_github_mcp["github-mcp"]
  skills_google_my_business["google-my-business"]
  skills_i18n_localization["i18n-localization"]
  skills_intelligent_routing["intelligent-routing"]
  skills_launch_strategy["launch-strategy"]
  skills_lint_and_validate["lint-and-validate"]
  skills_local_seo["local-seo"]
  skills_marketing_ideas["marketing-ideas"]
  skills_marketing_psychology["marketing-psychology"]
  skills_mcp_builder["mcp-builder"]
  skills_ml_engineer["ml-engineer"]
  skills_mobile_design["mobile-design"]
  skills_nextjs_react_expert["nextjs-react-expert"]
  skills_nodejs_best_practices["nodejs-best-practices"]
  skills_notebooklm_rag["notebooklm-rag"]
  skills_onboarding_cro["onboarding-cro"]
  skills_page_cro["page-cro"]
  skills_paid_ads["paid-ads"]
  skills_parallel_agents["parallel-agents"]
  skills_paywall_upgrade_cro["paywall-upgrade-cro"]
  skills_performance_profiling["performance-profiling"]
  skills_plan_writing["plan-writing"]
  skills_popup_cro["popup-cro"]
  skills_powershell_windows["powershell-windows"]
  skills_pricing_strategy["pricing-strategy"]
  skills_product_marketing_context["product-marketing-context"]
  skills_programmatic_seo["programmatic-seo"]
  skills_prompt_engineering["prompt-engineering"]
  skills_python_patterns["python-patterns"]
  skills_react_native_guidelines["react-native-guidelines"]
  skills_receiving_code_review["receiving-code-review"]
  skills_red_team_tactics["red-team-tactics"]
  skills_referral_program["referral-program"]
  skills_requesting_code_review["requesting-code-review"]
  skills_rust_pro["rust-pro"]
  skills_schema_markup["schema-markup"]
  skills_seo_audit["seo-audit"]
  skills_seo_fundamentals["seo-fundamentals"]
  skills_server_management["server-management"]
  skills_signup_flow_cro["signup-flow-cro"]
  skills_social_content["social-content"]
  skills_subagent_driven_development["subagent-driven-development"]
  skills_systematic_debugging["systematic-debugging"]
  skills_tailwind_patterns["tailwind-patterns"]
  skills_tdd_workflow["tdd-workflow"]
  skills_testing_patterns["testing-patterns"]
  skills_typeorm_patterns["typeorm-patterns"]
  skills_using_git_worktrees["using-git-worktrees"]
  skills_verification_before_completion["verification-before-completion"]
  skills_vulnerability_scanner["vulnerability-scanner"]
  skills_web_design_guidelines["web-design-guidelines"]
  skills_web3_smart_contracts["web3-smart-contracts"]
  skills_webapp_testing["webapp-testing"]
  skills_wordpress_mcp_bundle["wordpress-mcp-bundle"]
  skills_wordpress_site_build["wordpress-site-build"]
  skills_writing_skills["writing-skills"]
  skills_writing_skills_render_graphs_js["render-graphs.js"]
  workflows["workflows"]
  root --> _shared
  _shared --> _shared_ui_ux_pro_max
  root --> agents
  root --> brands
  brands --> brands__industry_template
  brands --> brands__template
  brands --> brands_accounting
  brands --> brands_travel
  root --> docs
  root --> mcp_servers
  root --> profiles
  root --> rules
  root --> scripts
  scripts --> scripts_auto_preview_py
  scripts --> scripts_checklist_py
  scripts --> scripts_session_manager_py
  scripts --> scripts_verify_all_py
  scripts --> scripts_verify_boundary_py
  scripts --> scripts_wordpress_checklist_py
  root --> skills
  skills --> skills_ab_test_setup
  skills --> skills_ad_creative
  skills --> skills_ai_seo
  skills --> skills_analytics_tracking
  skills --> skills_api_patterns
  skills --> skills_app_builder
  skills --> skills_architecture
  skills --> skills_architecture_explorer
  skills --> skills_bash_linux
  skills --> skills_behavioral_modes
  skills --> skills_brainstorming
  skills --> skills_business_listing
  skills --> skills_churn_prevention
  skills --> skills_clean_code
  skills --> skills_client_communication
  skills --> skills_cloud_infrastructure
  skills --> skills_code_review_checklist
  skills --> skills_cold_email
  skills --> skills_competitor_alternatives
  skills --> skills_composition_patterns
  skills --> skills_content_strategy
  skills --> skills_copy_editing
  skills --> skills_copywriting
  skills --> skills_data_analysis
  skills --> skills_database_design
  skills --> skills_deployment_procedures
  skills --> skills_design_system_architecture
  skills --> skills_documentation_templates
  skills --> skills_email_sequence
  skills --> skills_envato_template_selection
  skills --> skills_executing_plans
  skills --> skills_finishing_a_development_branch
  skills --> skills_form_cro
  skills --> skills_free_tool_strategy
  skills --> skills_frontend_design
  skills --> skills_game_development
  skills --> skills_geo_fundamentals
  skills --> skills_github_mcp
  skills --> skills_google_my_business
  skills --> skills_i18n_localization
  skills --> skills_intelligent_routing
  skills --> skills_launch_strategy
  skills --> skills_lint_and_validate
  skills --> skills_local_seo
  skills --> skills_marketing_ideas
  skills --> skills_marketing_psychology
  skills --> skills_mcp_builder
  skills --> skills_ml_engineer
  skills --> skills_mobile_design
  skills --> skills_nextjs_react_expert
  skills --> skills_nodejs_best_practices
  skills --> skills_notebooklm_rag
  skills --> skills_onboarding_cro
  skills --> skills_page_cro
  skills --> skills_paid_ads
  skills --> skills_parallel_agents
  skills --> skills_paywall_upgrade_cro
  skills --> skills_performance_profiling
  skills --> skills_plan_writing
  skills --> skills_popup_cro
  skills --> skills_powershell_windows
  skills --> skills_pricing_strategy
  skills --> skills_product_marketing_context
  skills --> skills_programmatic_seo
  skills --> skills_prompt_engineering
  skills --> skills_python_patterns
  skills --> skills_react_native_guidelines
  skills --> skills_receiving_code_review
  skills --> skills_red_team_tactics
  skills --> skills_referral_program
  skills --> skills_requesting_code_review
  skills --> skills_rust_pro
  skills --> skills_schema_markup
  skills --> skills_seo_audit
  skills --> skills_seo_fundamentals
  skills --> skills_server_management
  skills --> skills_signup_flow_cro
  skills --> skills_social_content
  skills --> skills_subagent_driven_development
  skills --> skills_systematic_debugging
  skills --> skills_tailwind_patterns
  skills --> skills_tdd_workflow
  skills --> skills_testing_patterns
  skills --> skills_typeorm_patterns
  skills --> skills_using_git_worktrees
  skills --> skills_verification_before_completion
  skills --> skills_vulnerability_scanner
  skills --> skills_web_design_guidelines
  skills --> skills_web3_smart_contracts
  skills --> skills_webapp_testing
  skills --> skills_wordpress_mcp_bundle
  skills --> skills_wordpress_site_build
  skills --> skills_writing_skills
  skills_writing_skills --> skills_writing_skills_render_graphs_js
  root --> workflows
  click root "file:///nara/projectCA/.agent" "Open .agent"
  click _shared "file:///nara/projectCA/.agent/.shared" "Open .shared"
  click _shared_ui_ux_pro_max "file:///nara/projectCA/.agent/.shared/ui-ux-pro-max" "Open ui-ux-pro-max"
  click agents "file:///nara/projectCA/.agent/agents" "Open agents"
  click brands "file:///nara/projectCA/.agent/brands" "Open brands"
  click brands__industry_template "file:///nara/projectCA/.agent/brands/_industry-template" "Open _industry-template"
  click brands__template "file:///nara/projectCA/.agent/brands/_template" "Open _template"
  click brands_accounting "file:///nara/projectCA/.agent/brands/accounting" "Open accounting"
  click brands_travel "file:///nara/projectCA/.agent/brands/travel" "Open travel"
  click docs "file:///nara/projectCA/.agent/docs" "Open docs"
  click mcp_servers "file:///nara/projectCA/.agent/mcp-servers" "Open mcp-servers"
  click profiles "file:///nara/projectCA/.agent/profiles" "Open profiles"
  click rules "file:///nara/projectCA/.agent/rules" "Open rules"
  click scripts "file:///nara/projectCA/.agent/scripts" "Open scripts"
  click scripts_auto_preview_py "file:///nara/projectCA/.agent/scripts/auto_preview.py" "Open auto_preview.py"
  click scripts_checklist_py "file:///nara/projectCA/.agent/scripts/checklist.py" "Open checklist.py"
  click scripts_session_manager_py "file:///nara/projectCA/.agent/scripts/session_manager.py" "Open session_manager.py"
  click scripts_verify_all_py "file:///nara/projectCA/.agent/scripts/verify_all.py" "Open verify_all.py"
  click scripts_verify_boundary_py "file:///nara/projectCA/.agent/scripts/verify_boundary.py" "Open verify_boundary.py"
  click scripts_wordpress_checklist_py "file:///nara/projectCA/.agent/scripts/wordpress_checklist.py" "Open wordpress_checklist.py"
  click skills "file:///nara/projectCA/.agent/skills" "Open skills"
  click skills_ab_test_setup "file:///nara/projectCA/.agent/skills/ab-test-setup" "Open ab-test-setup"
  click skills_ad_creative "file:///nara/projectCA/.agent/skills/ad-creative" "Open ad-creative"
  click skills_ai_seo "file:///nara/projectCA/.agent/skills/ai-seo" "Open ai-seo"
  click skills_analytics_tracking "file:///nara/projectCA/.agent/skills/analytics-tracking" "Open analytics-tracking"
  click skills_api_patterns "file:///nara/projectCA/.agent/skills/api-patterns" "Open api-patterns"
  click skills_app_builder "file:///nara/projectCA/.agent/skills/app-builder" "Open app-builder"
  click skills_architecture "file:///nara/projectCA/.agent/skills/architecture" "Open architecture"
  click skills_architecture_explorer "file:///nara/projectCA/.agent/skills/architecture-explorer" "Open architecture-explorer"
  click skills_bash_linux "file:///nara/projectCA/.agent/skills/bash-linux" "Open bash-linux"
  click skills_behavioral_modes "file:///nara/projectCA/.agent/skills/behavioral-modes" "Open behavioral-modes"
  click skills_brainstorming "file:///nara/projectCA/.agent/skills/brainstorming" "Open brainstorming"
  click skills_business_listing "file:///nara/projectCA/.agent/skills/business-listing" "Open business-listing"
  click skills_churn_prevention "file:///nara/projectCA/.agent/skills/churn-prevention" "Open churn-prevention"
  click skills_clean_code "file:///nara/projectCA/.agent/skills/clean-code" "Open clean-code"
  click skills_client_communication "file:///nara/projectCA/.agent/skills/client-communication" "Open client-communication"
  click skills_cloud_infrastructure "file:///nara/projectCA/.agent/skills/cloud-infrastructure" "Open cloud-infrastructure"
  click skills_code_review_checklist "file:///nara/projectCA/.agent/skills/code-review-checklist" "Open code-review-checklist"
  click skills_cold_email "file:///nara/projectCA/.agent/skills/cold-email" "Open cold-email"
  click skills_competitor_alternatives "file:///nara/projectCA/.agent/skills/competitor-alternatives" "Open competitor-alternatives"
  click skills_composition_patterns "file:///nara/projectCA/.agent/skills/composition-patterns" "Open composition-patterns"
  click skills_content_strategy "file:///nara/projectCA/.agent/skills/content-strategy" "Open content-strategy"
  click skills_copy_editing "file:///nara/projectCA/.agent/skills/copy-editing" "Open copy-editing"
  click skills_copywriting "file:///nara/projectCA/.agent/skills/copywriting" "Open copywriting"
  click skills_data_analysis "file:///nara/projectCA/.agent/skills/data-analysis" "Open data-analysis"
  click skills_database_design "file:///nara/projectCA/.agent/skills/database-design" "Open database-design"
  click skills_deployment_procedures "file:///nara/projectCA/.agent/skills/deployment-procedures" "Open deployment-procedures"
  click skills_design_system_architecture "file:///nara/projectCA/.agent/skills/design-system-architecture" "Open design-system-architecture"
  click skills_documentation_templates "file:///nara/projectCA/.agent/skills/documentation-templates" "Open documentation-templates"
  click skills_email_sequence "file:///nara/projectCA/.agent/skills/email-sequence" "Open email-sequence"
  click skills_envato_template_selection "file:///nara/projectCA/.agent/skills/envato-template-selection" "Open envato-template-selection"
  click skills_executing_plans "file:///nara/projectCA/.agent/skills/executing-plans" "Open executing-plans"
  click skills_finishing_a_development_branch "file:///nara/projectCA/.agent/skills/finishing-a-development-branch" "Open finishing-a-development-branch"
  click skills_form_cro "file:///nara/projectCA/.agent/skills/form-cro" "Open form-cro"
  click skills_free_tool_strategy "file:///nara/projectCA/.agent/skills/free-tool-strategy" "Open free-tool-strategy"
  click skills_frontend_design "file:///nara/projectCA/.agent/skills/frontend-design" "Open frontend-design"
  click skills_game_development "file:///nara/projectCA/.agent/skills/game-development" "Open game-development"
  click skills_geo_fundamentals "file:///nara/projectCA/.agent/skills/geo-fundamentals" "Open geo-fundamentals"
  click skills_github_mcp "file:///nara/projectCA/.agent/skills/github-mcp" "Open github-mcp"
  click skills_google_my_business "file:///nara/projectCA/.agent/skills/google-my-business" "Open google-my-business"
  click skills_i18n_localization "file:///nara/projectCA/.agent/skills/i18n-localization" "Open i18n-localization"
  click skills_intelligent_routing "file:///nara/projectCA/.agent/skills/intelligent-routing" "Open intelligent-routing"
  click skills_launch_strategy "file:///nara/projectCA/.agent/skills/launch-strategy" "Open launch-strategy"
  click skills_lint_and_validate "file:///nara/projectCA/.agent/skills/lint-and-validate" "Open lint-and-validate"
  click skills_local_seo "file:///nara/projectCA/.agent/skills/local-seo" "Open local-seo"
  click skills_marketing_ideas "file:///nara/projectCA/.agent/skills/marketing-ideas" "Open marketing-ideas"
  click skills_marketing_psychology "file:///nara/projectCA/.agent/skills/marketing-psychology" "Open marketing-psychology"
  click skills_mcp_builder "file:///nara/projectCA/.agent/skills/mcp-builder" "Open mcp-builder"
  click skills_ml_engineer "file:///nara/projectCA/.agent/skills/ml-engineer" "Open ml-engineer"
  click skills_mobile_design "file:///nara/projectCA/.agent/skills/mobile-design" "Open mobile-design"
  click skills_nextjs_react_expert "file:///nara/projectCA/.agent/skills/nextjs-react-expert" "Open nextjs-react-expert"
  click skills_nodejs_best_practices "file:///nara/projectCA/.agent/skills/nodejs-best-practices" "Open nodejs-best-practices"
  click skills_notebooklm_rag "file:///nara/projectCA/.agent/skills/notebooklm-rag" "Open notebooklm-rag"
  click skills_onboarding_cro "file:///nara/projectCA/.agent/skills/onboarding-cro" "Open onboarding-cro"
  click skills_page_cro "file:///nara/projectCA/.agent/skills/page-cro" "Open page-cro"
  click skills_paid_ads "file:///nara/projectCA/.agent/skills/paid-ads" "Open paid-ads"
  click skills_parallel_agents "file:///nara/projectCA/.agent/skills/parallel-agents" "Open parallel-agents"
  click skills_paywall_upgrade_cro "file:///nara/projectCA/.agent/skills/paywall-upgrade-cro" "Open paywall-upgrade-cro"
  click skills_performance_profiling "file:///nara/projectCA/.agent/skills/performance-profiling" "Open performance-profiling"
  click skills_plan_writing "file:///nara/projectCA/.agent/skills/plan-writing" "Open plan-writing"
  click skills_popup_cro "file:///nara/projectCA/.agent/skills/popup-cro" "Open popup-cro"
  click skills_powershell_windows "file:///nara/projectCA/.agent/skills/powershell-windows" "Open powershell-windows"
  click skills_pricing_strategy "file:///nara/projectCA/.agent/skills/pricing-strategy" "Open pricing-strategy"
  click skills_product_marketing_context "file:///nara/projectCA/.agent/skills/product-marketing-context" "Open product-marketing-context"
  click skills_programmatic_seo "file:///nara/projectCA/.agent/skills/programmatic-seo" "Open programmatic-seo"
  click skills_prompt_engineering "file:///nara/projectCA/.agent/skills/prompt-engineering" "Open prompt-engineering"
  click skills_python_patterns "file:///nara/projectCA/.agent/skills/python-patterns" "Open python-patterns"
  click skills_react_native_guidelines "file:///nara/projectCA/.agent/skills/react-native-guidelines" "Open react-native-guidelines"
  click skills_receiving_code_review "file:///nara/projectCA/.agent/skills/receiving-code-review" "Open receiving-code-review"
  click skills_red_team_tactics "file:///nara/projectCA/.agent/skills/red-team-tactics" "Open red-team-tactics"
  click skills_referral_program "file:///nara/projectCA/.agent/skills/referral-program" "Open referral-program"
  click skills_requesting_code_review "file:///nara/projectCA/.agent/skills/requesting-code-review" "Open requesting-code-review"
  click skills_rust_pro "file:///nara/projectCA/.agent/skills/rust-pro" "Open rust-pro"
  click skills_schema_markup "file:///nara/projectCA/.agent/skills/schema-markup" "Open schema-markup"
  click skills_seo_audit "file:///nara/projectCA/.agent/skills/seo-audit" "Open seo-audit"
  click skills_seo_fundamentals "file:///nara/projectCA/.agent/skills/seo-fundamentals" "Open seo-fundamentals"
  click skills_server_management "file:///nara/projectCA/.agent/skills/server-management" "Open server-management"
  click skills_signup_flow_cro "file:///nara/projectCA/.agent/skills/signup-flow-cro" "Open signup-flow-cro"
  click skills_social_content "file:///nara/projectCA/.agent/skills/social-content" "Open social-content"
  click skills_subagent_driven_development "file:///nara/projectCA/.agent/skills/subagent-driven-development" "Open subagent-driven-development"
  click skills_systematic_debugging "file:///nara/projectCA/.agent/skills/systematic-debugging" "Open systematic-debugging"
  click skills_tailwind_patterns "file:///nara/projectCA/.agent/skills/tailwind-patterns" "Open tailwind-patterns"
  click skills_tdd_workflow "file:///nara/projectCA/.agent/skills/tdd-workflow" "Open tdd-workflow"
  click skills_testing_patterns "file:///nara/projectCA/.agent/skills/testing-patterns" "Open testing-patterns"
  click skills_typeorm_patterns "file:///nara/projectCA/.agent/skills/typeorm-patterns" "Open typeorm-patterns"
  click skills_using_git_worktrees "file:///nara/projectCA/.agent/skills/using-git-worktrees" "Open using-git-worktrees"
  click skills_verification_before_completion "file:///nara/projectCA/.agent/skills/verification-before-completion" "Open verification-before-completion"
  click skills_vulnerability_scanner "file:///nara/projectCA/.agent/skills/vulnerability-scanner" "Open vulnerability-scanner"
  click skills_web_design_guidelines "file:///nara/projectCA/.agent/skills/web-design-guidelines" "Open web-design-guidelines"
  click skills_web3_smart_contracts "file:///nara/projectCA/.agent/skills/web3-smart-contracts" "Open web3-smart-contracts"
  click skills_webapp_testing "file:///nara/projectCA/.agent/skills/webapp-testing" "Open webapp-testing"
  click skills_wordpress_mcp_bundle "file:///nara/projectCA/.agent/skills/wordpress-mcp-bundle" "Open wordpress-mcp-bundle"
  click skills_wordpress_site_build "file:///nara/projectCA/.agent/skills/wordpress-site-build" "Open wordpress-site-build"
  click skills_writing_skills "file:///nara/projectCA/.agent/skills/writing-skills" "Open writing-skills"
  click skills_writing_skills_render_graphs_js "file:///nara/projectCA/.agent/skills/writing-skills/render-graphs.js" "Open render-graphs.js"
  click workflows "file:///nara/projectCA/.agent/workflows" "Open workflows"
```
