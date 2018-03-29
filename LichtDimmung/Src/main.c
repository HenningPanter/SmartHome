/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * This notice applies to any and all portions of this file
  * that are not between comment pairs USER CODE BEGIN and
  * USER CODE END. Other portions of this file, whether 
  * inserted by the user or by software development tools
  * are owned by their respective copyright owners.
  *
  * Copyright (c) 2018 STMicroelectronics International N.V. 
  * All rights reserved.
  *
  * Redistribution and use in source and binary forms, with or without 
  * modification, are permitted, provided that the following conditions are met:
  *
  * 1. Redistribution of source code must retain the above copyright notice, 
  *    this list of conditions and the following disclaimer.
  * 2. Redistributions in binary form must reproduce the above copyright notice,
  *    this list of conditions and the following disclaimer in the documentation
  *    and/or other materials provided with the distribution.
  * 3. Neither the name of STMicroelectronics nor the names of other 
  *    contributors to this software may be used to endorse or promote products 
  *    derived from this software without specific written permission.
  * 4. This software, including modifications and/or derivative works of this 
  *    software, must execute solely and exclusively on microcontroller or
  *    microprocessor devices manufactured by or for STMicroelectronics.
  * 5. Redistribution and use of this software other than as permitted under 
  *    this license is void and will automatically terminate your rights under 
  *    this license. 
  *
  * THIS SOFTWARE IS PROVIDED BY STMICROELECTRONICS AND CONTRIBUTORS "AS IS" 
  * AND ANY EXPRESS, IMPLIED OR STATUTORY WARRANTIES, INCLUDING, BUT NOT 
  * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
  * PARTICULAR PURPOSE AND NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY
  * RIGHTS ARE DISCLAIMED TO THE FULLEST EXTENT PERMITTED BY LAW. IN NO EVENT 
  * SHALL STMICROELECTRONICS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
  * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
  * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
  * OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
  * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
  * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
  * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  *
  ******************************************************************************
  */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32f1xx_hal.h"
#include "cmsis_os.h"

/* USER CODE BEGIN Includes */

#include "stdbool.h"
#include "string.h"

/* USER CODE END Includes */

/* Private variables ---------------------------------------------------------*/
TIM_HandleTypeDef htim2;

UART_HandleTypeDef huart1;

osThreadId PwmTaskHandle;
osThreadId UartTaskHandle;
osMessageQId myQueue01Handle;

/* USER CODE BEGIN PV */
/* Private variables ---------------------------------------------------------*/

bool bNewFrame;
uint8_t Frame[FrameSize];
uint8_t TestString[20];
uint16_t Tabelle[100] = {0,5,10,20,30,40,50,60,70,80,90,10,120,140,160,180,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1200,1300,1400,1500,1600,1700,1800,1900,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800,4000,4200,4400,4600,4800,5000,5200,5400,5600,5800,6000,6200,6400,6600,6800,7000,7200,7400,7600,7800,8000,8200,8400,8600,8800,9000,9200,9400,9600,9800,10000,10200,10400,10600,10800,11000,11200,11400,11600,11800,12000,12200,12400,12600,12800,13000,13200,13400,13513};

uint32_t Weiss = 0,Rot = 0, Gruen = 0, Blau = 0;

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_TIM2_Init(void);
static void MX_USART1_UART_Init(void);
void Task_1(void const * argument);
void Task_2(void const * argument);                                    
void HAL_TIM_MspPostInit(TIM_HandleTypeDef *htim);
void ProzessFrame(void);
                                

/* USER CODE BEGIN PFP */
/* Private function prototypes -----------------------------------------------*/

/* USER CODE END PFP */

/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  *
  * @retval None
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration----------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_TIM2_Init();
  MX_USART1_UART_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* USER CODE BEGIN RTOS_MUTEX */
	/* add mutexes, ... */
  /* USER CODE END RTOS_MUTEX */

  /* USER CODE BEGIN RTOS_SEMAPHORES */
	/* add semaphores, ... */
  /* USER CODE END RTOS_SEMAPHORES */

  /* USER CODE BEGIN RTOS_TIMERS */
	/* start timers, add new ones, ... */
  /* USER CODE END RTOS_TIMERS */

  /* Create the thread(s) */
  /* definition and creation of PwmTask */
  osThreadDef(PwmTask, Task_1, osPriorityNormal, 0, 128);
  PwmTaskHandle = osThreadCreate(osThread(PwmTask), NULL);

  /* definition and creation of UartTask */
  osThreadDef(UartTask, Task_2, osPriorityIdle, 0, 128);
  UartTaskHandle = osThreadCreate(osThread(UartTask), NULL);

  /* USER CODE BEGIN RTOS_THREADS */
	/* add threads, ... */
  /* USER CODE END RTOS_THREADS */

  /* Create the queue(s) */
  /* definition and creation of myQueue01 */
  osMessageQDef(myQueue01, 16, uint16_t);
  myQueue01Handle = osMessageCreate(osMessageQ(myQueue01), NULL);

  /* USER CODE BEGIN RTOS_QUEUES */
	/* add queues, ... */
  /* USER CODE END RTOS_QUEUES */
 

  /* Start scheduler */
  osKernelStart();
  
  /* We should never get here as control is now taken by the scheduler */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
	while (1) {
  /* USER CODE END WHILE */

  /* USER CODE BEGIN 3 */

	}
  /* USER CODE END 3 */

}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{

  RCC_OscInitTypeDef RCC_OscInitStruct;
  RCC_ClkInitTypeDef RCC_ClkInitStruct;

    /**Initializes the CPU, AHB and APB busses clocks 
    */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

    /**Initializes the CPU, AHB and APB busses clocks 
    */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

    /**Configure the Systick interrupt time 
    */
  HAL_SYSTICK_Config(HAL_RCC_GetHCLKFreq()/1000);

    /**Configure the Systick 
    */
  HAL_SYSTICK_CLKSourceConfig(SYSTICK_CLKSOURCE_HCLK);

  /* SysTick_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(SysTick_IRQn, 15, 0);
}

/* TIM2 init function */
static void MX_TIM2_Init(void)
{

  TIM_MasterConfigTypeDef sMasterConfig;
  TIM_OC_InitTypeDef sConfigOC;

  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 15;
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 13513;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_PWM_Init(&htim2) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_2) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_3) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_4) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

  HAL_TIM_MspPostInit(&htim2);

}

/* USART1 init function */
static void MX_USART1_UART_Init(void)
{

  huart1.Instance = USART1;
  huart1.Init.BaudRate = 115200;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

}

/** Configure pins as 
        * Analog 
        * Input 
        * Output
        * EVENT_OUT
        * EXTI
*/
static void MX_GPIO_Init(void)
{

  GPIO_InitTypeDef GPIO_InitStruct;

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_RESET);

  /*Configure GPIO pin : PC13 */
  GPIO_InitStruct.Pin = GPIO_PIN_13;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

void Init(void) {
	uint8_t i;
	bNewFrame = false;

	for (i = 0; i < FrameSize; i++) {
		Frame[i] = 0;
		TestString[i] = 0;
	}

	htim2.Instance->CCR1 = 0;		// Weiß
	htim2.Instance->CCR2 = 0;		// Rot
	htim2.Instance->CCR3 = 0;	 	// Grün
	htim2.Instance->CCR4 = 0;	// Blau
}

bool CheckFrame(void) {
	if(Frame[0] == 48 && Frame[1] == 49 && Frame[2] == 50 && Frame[3] == 51 && Frame[4] == 52 && Frame[5] == 53 && Frame[6] == 54 && Frame[7] == 55 && Frame[8] == 56 && Frame[9] == 57)
	{
		ProzessFrame();
		return true;
	}
	return false;
}

void ProzessFrame(void) {

	HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);

	// Weiß:
	if(Frame[10] > 99) {
		Frame[10] = 99;
	}
	Weiss = Tabelle[Frame[10]];
//	htim2.Instance->CCR1 = Tabelle[Frame[10]];

	// Rot:
	if(Frame[11] > 99) {
		Frame[11] = 99;
	}
	Rot = Tabelle[Frame[11]];
//	htim2.Instance->CCR2 = Tabelle[Frame[11]];

	// Grün:
	if(Frame[12] > 99) {
		Frame[12] = 99;
	}
	Gruen = Tabelle[Frame[12]];
//	htim2.Instance->CCR3 = Tabelle[Frame[12]];

	// Blau:
	if(Frame[13] > 99) {
		Frame[13] = 99;
	}
	Blau = Tabelle[Frame[13]];
//	htim2.Instance->CCR4 = Tabelle[Frame[13]];
}

/* USER CODE END 4 */

/* StartDefaultTask function */
void Task_1(void const * argument)
{

  /* USER CODE BEGIN 5 */

	uint32_t Delta = 0;

	/* Infinite loop */
	for (;;) {
		osDelay(1);

		if(htim2.Instance->CCR1 < Weiss)
		{
			Delta = Weiss - htim2.Instance->CCR1;

			if(Delta > 500)
			{
				htim2.Instance->CCR1 += Delta/100;
			}
			else
			{
				htim2.Instance->CCR1 ++;
			}

		}
		if(htim2.Instance->CCR1 > Weiss)
		{
			Delta = htim2.Instance->CCR1 - Weiss;

			if(Delta > 500)
			{
				htim2.Instance->CCR1 -= Delta/100;
			}
			else
			{
				htim2.Instance->CCR1 --;
			}
		}




		if(htim2.Instance->CCR2 < Rot)
		{
			Delta = Rot - htim2.Instance->CCR2;

			if(Delta > 500)
			{
				htim2.Instance->CCR2 += Delta/100;
			}
			else
			{
				htim2.Instance->CCR2 ++;
			}
		}
		if(htim2.Instance->CCR2 > Rot)
		{
			Delta = htim2.Instance->CCR2 - Rot;

			if(Delta > 500)
			{
				htim2.Instance->CCR2 -= Delta/100;
			}
			else
			{
				htim2.Instance->CCR2 --;
			}
		}







		if(htim2.Instance->CCR3 < Gruen)
		{
			Delta = Gruen - htim2.Instance->CCR3;

			if(Delta > 500)
			{
				htim2.Instance->CCR3 += Delta/100;
			}
			else
			{
				htim2.Instance->CCR3 ++;
			}
		}
		if(htim2.Instance->CCR3 > Gruen)
		{
			Delta = htim2.Instance->CCR3 - Gruen;

			if(Delta > 500)
			{
				htim2.Instance->CCR3 -= Delta/100;
			}
			else
			{
				htim2.Instance->CCR3 --;
			}
		}










		if(htim2.Instance->CCR4 < Blau)
		{
			Delta = Blau - htim2.Instance->CCR4;

			if(Delta > 500)
			{
				htim2.Instance->CCR4 += Delta/100;
			}
			else
			{
				htim2.Instance->CCR4 ++;
			}
		}
		if(htim2.Instance->CCR4 > Blau)
		{
			Delta = htim2.Instance->CCR4 - Blau;

			if(Delta > 500)
			{
				htim2.Instance->CCR4 -= Delta/100;
			}
			else
			{
				htim2.Instance->CCR4 --;
			}
		}

//		HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);

	}
  /* USER CODE END 5 */ 
}

/* StartTask02 function */
void Task_2(void const * argument)
{
  /* USER CODE BEGIN StartTask02 */
	static uint8_t ucIndex = 0;
	static uint32_t uRxTimeOutValue = 0;
	uint8_t Value = 0;
	char Answer[10];


//	htim2.Init.Prescaler = 15;
//	htim2.Init.Period = 13513;

	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_2);
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_3);
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_4);

	Init();

	/* Infinite loop */
	for (;;) {

		if((huart1.Instance->SR & 0x20) == 0x20)
		{
			HAL_UART_Receive(&huart1, &Value, 1, 1);
			Frame[ucIndex] = Value;
			ucIndex++;
			uRxTimeOutValue = HAL_GetTick();
		}
//    osDelay(500);


		if (ucIndex == FrameSize) {
			ucIndex = 0;
			if(CheckFrame()) {
				strncpy(Answer, "OK\n\r", 4);
				HAL_UART_Transmit(&huart1, (uint8_t*)Answer, strlen(Answer), 10);
			}
			else {
				strncpy(Answer, "FAIL\n\r", 6);
				HAL_UART_Transmit(&huart1, (uint8_t*)Answer, strlen(Answer), 10);
			}
		}

		if ((HAL_GetTick() - uRxTimeOutValue) > RxTimeOut) {
			ucIndex = 0;
		}

	}
  /* USER CODE END StartTask02 */
}

/**
  * @brief  Period elapsed callback in non blocking mode
  * @note   This function is called  when TIM1 interrupt took place, inside
  * HAL_TIM_IRQHandler(). It makes a direct call to HAL_IncTick() to increment
  * a global variable "uwTick" used as application time base.
  * @param  htim : TIM handle
  * @retval None
  */
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
  /* USER CODE BEGIN Callback 0 */

  /* USER CODE END Callback 0 */
  if (htim->Instance == TIM1) {
    HAL_IncTick();
  }
  /* USER CODE BEGIN Callback 1 */

  /* USER CODE END Callback 1 */
}

/**
  * @brief  This function is executed in case of error occurrence.
  * @param  file: The file name as string.
  * @param  line: The line in file as a number.
  * @retval None
  */
void _Error_Handler(char *file, int line)
{
  /* USER CODE BEGIN Error_Handler_Debug */
	/* User can add his own implementation to report the HAL error return state */
	while (1) {
	}
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t* file, uint32_t line)
{ 
  /* USER CODE BEGIN 6 */
	/* User can add his own implementation to report the file name and line number,
	 ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/**
  * @}
  */

/**
  * @}
  */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
