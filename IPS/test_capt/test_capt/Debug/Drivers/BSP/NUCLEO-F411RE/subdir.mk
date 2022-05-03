################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/BSP/NUCLEO-F411RE/uart_trace.c \
../Drivers/BSP/NUCLEO-F411RE/vl53l0x_platform.c 

OBJS += \
./Drivers/BSP/NUCLEO-F411RE/uart_trace.o \
./Drivers/BSP/NUCLEO-F411RE/vl53l0x_platform.o 

C_DEPS += \
./Drivers/BSP/NUCLEO-F411RE/uart_trace.d \
./Drivers/BSP/NUCLEO-F411RE/vl53l0x_platform.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/NUCLEO-F411RE/%.o: ../Drivers/BSP/NUCLEO-F411RE/%.c Drivers/BSP/NUCLEO-F411RE/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F411xE -c -I"C:/Users/romai/OneDrive/Bureau/Enib S7/IPS/test_capt/test_capt/Drivers/BSP/Components/vl53l0x" -I../Core/Inc -I"C:/Users/romai/OneDrive/Bureau/Enib S7/IPS/test_capt/test_capt/Drivers/BSP/NUCLEO-F411RE" -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-BSP-2f-NUCLEO-2d-F411RE

clean-Drivers-2f-BSP-2f-NUCLEO-2d-F411RE:
	-$(RM) ./Drivers/BSP/NUCLEO-F411RE/uart_trace.d ./Drivers/BSP/NUCLEO-F411RE/uart_trace.o ./Drivers/BSP/NUCLEO-F411RE/vl53l0x_platform.d ./Drivers/BSP/NUCLEO-F411RE/vl53l0x_platform.o

.PHONY: clean-Drivers-2f-BSP-2f-NUCLEO-2d-F411RE

