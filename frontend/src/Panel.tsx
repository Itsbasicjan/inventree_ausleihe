import { MantineProvider, Stack, Text, Title } from '@mantine/core';
import { createRoot } from 'react-dom/client';
import { useMemo } from 'react';

/**
 * Render a custom panel with the provided context.
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/stable/extend/plugins/ui/#plugin-context
 */
function AusleihfunktionPanel({
    context
}: {
    context: any;
}) {

    // Extract context information
    const instance: string = useMemo(() => {
        let data = context?.instance ?? {};
        return JSON.stringify(data, null, 2);
    }, [context.instance]);

    return (
        <>
        <Stack gap="xs">
        <Title order={3}>Ausleihfunktion</Title>
        <Text>
            This is a custom panel for the Ausleihfunktion plugin.
        </Text>
        <Title order={5}>Instance Data</Title>
        <div>
            {instance}
        </div>
        </Stack>
        </>
    );
}


/**
 * Render the AusleihfunktionPanel component.
 * 
 * @param target - The target HTML element to render the panel into
 * @param context - The context object to pass to the panel
 */
export function renderAusleihfunktionPanel(target: HTMLElement, context: any) {
    createRoot(target).render(
        <MantineProvider>
            <AusleihfunktionPanel context={context} />
        </MantineProvider>
    );
}
